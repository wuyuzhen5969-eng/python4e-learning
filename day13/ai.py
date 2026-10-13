import os
import subprocess
import ollama

MODEL = "qwen2.5:7b"       # 先执行: ollama pull qwen2.5:7b (也可换成 llama3.1:8b)
MAX_STEPS = 10             # 单次提问内,模型最多连续调用工具的轮数
MAX_OUTPUT_CHARS = 5000    # 工具返回内容的最大长度,防止撑爆上下文
WORKSPACE = os.path.abspath(".")  # 所有文件操作限制在这个目录内

system_prompt = f"""
You are a coding assistant. Your working directory is: {WORKSPACE}
Rules:
- Always use RELATIVE paths such as "snake_game/main.py". Never use absolute paths.
- write_file needs BOTH "path" (a file, not a directory) and "content" (the full source code only, no chat text).
- Directories are created automatically by write_file, so never try to create a directory by itself.
- After writing, verify the file exists with list_files.
- Never say a file was created unless write_file returned "saved ...".
- To run a program, use run_command (the user will be asked for approval).
- Call tools through the real tool-calling mechanism, never by writing JSON as plain text.
"""


# ---------- 工具函数 ----------

def truncate(text, limit=MAX_OUTPUT_CHARS):
    if len(text) > limit:
        return text[:limit] + f"\n...(truncated, {len(text) - limit} more characters)"
    return text


def safe_path(path):
    """把路径解析到 WORKSPACE 内,禁止跳出工作目录。"""
    full = os.path.abspath(os.path.join(WORKSPACE, path))
    if os.path.commonpath([WORKSPACE, full]) != WORKSPACE:
        raise ValueError(f"path '{path}' is outside the workspace; use a relative path")
    return full


def list_files(path="."):
    full = safe_path(path)
    with os.scandir(full) as it:
        entries = [e.name + ("/" if e.is_dir() else "") for e in it]
    return "\n".join(sorted(entries)) or "(empty directory)"


def read_file(path):
    with open(safe_path(path), "r", encoding="utf-8") as f:
        return truncate(f.read())


def write_file(path, content):
    full = safe_path(path)
    if os.path.isdir(full):
        raise IsADirectoryError(f"'{path}' is a directory; give a file path such as '{path}/main.py'")
    os.makedirs(os.path.dirname(full), exist_ok=True)  # 目录不存在时自动创建
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    return f"saved {path} ({len(content)} characters)"


def run_command(command):
    answer = input(f"Run '{command}'? [y/N] ")
    if answer.strip().lower() != "y":
        return "The user declined to run this command."
    try:
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True,
            timeout=120, cwd=WORKSPACE,
        )
    except subprocess.TimeoutExpired:
        return "Error: command timed out after 120 seconds."
    output = (result.stdout + result.stderr).strip()
    return truncate(output) if output else f"(no output, exit code {result.returncode})"


TOOLS = {
    "list_files": list_files,
    "read_file": read_file,
    "write_file": write_file,
    "run_command": run_command,
}

TOOL_SCHEMAS = [{
    "type": "function",
    "function": {
        "name": "list_files",
        "description": "List the files in a directory. Folders end with /.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Directory to list, e.g. '.'"}
            },
            "required": []
        }
    }
}, {
    "type": "function",
    "function": {
        "name": "read_file",
        "description": "Read a text file and return its content.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Path of the file to read."}
            },
            "required": ["path"]
        }
    }
}, {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Create or overwrite a text file with the given content. Parent directories are created automatically.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Path of the file to write, e.g. 'snake_game/main.py'."},
                "content": {"type": "string", "description": "Full contents of the file."}
            },
            "required": ["path", "content"]
        }
    }
}, {
    "type": "function",
    "function": {
        "name": "run_command",
        "description": "Run a shell command and return its output. The user approves it first.",
        "parameters": {
            "type": "object",
            "properties": {
                "command": {"type": "string", "description": "The shell command to run."}
            },
            "required": ["command"]
        }
    }
}]

# 每个工具的必填参数,用于报错时提示模型
REQUIRED_PARAMS = {
    s["function"]["name"]: s["function"]["parameters"]["required"]
    for s in TOOL_SCHEMAS
}


# ---------- 执行工具 ----------

def run_tool(tool_call):
    name = tool_call.function.name
    args = tool_call.function.arguments or {}
    print(f"tool: {name}({args})")
    if name not in TOOLS:
        return f"Error: unknown tool '{name}'. Available tools: {', '.join(TOOLS)}"
    try:
        return str(TOOLS[name](**args))
    except TypeError as error:
        return (f"Error: wrong arguments for '{name}': {error}. "
                f"Call the tool again with all required parameters: {REQUIRED_PARAMS[name]}")
    except Exception as error:
        return f"Error: {type(error).__name__}: {error}"


# ---------- 一次 agent 运行(处理一条用户输入) ----------

def run_agent(messages):
    for _ in range(MAX_STEPS):
        try:
            response = ollama.chat(
                model=MODEL,
                messages=messages,
                tools=TOOL_SCHEMAS,
            )
        except Exception as error:
            return (f"[Failed to call Ollama: {error}]\n"
                    f"Check that Ollama is running and the model is installed "
                    f"(ollama pull {MODEL}).")

        message = response.message
        messages.append(message)

        if not message.tool_calls:
            text = (message.content or "").strip()
            # 兜底:模型把工具调用当成普通文本输出了
            if text.startswith("{") and '"name"' in text:
                messages.append({
                    "role": "user",
                    "content": "You wrote a tool call as plain text, so nothing was executed. "
                               "Use the real tool-calling mechanism instead.",
                })
                continue
            return message.content

        for tool_call in message.tool_calls:
            result = run_tool(tool_call)
            messages.append({
                "role": "tool",
                "tool_name": tool_call.function.name,
                "content": result,
            })

    return f"[Stopped: reached the limit of {MAX_STEPS} tool-call rounds.]"


# ---------- 主程序 ----------

def main():
    messages = [{"role": "system", "content": system_prompt}]
    print(f"Mini agent ready (model: {MODEL}). Type exit to quit.")
    while True:
        try:
            user_input = input("\nYou: ")
        except (EOFError, KeyboardInterrupt):
            print("\nBye.")
            break
        if user_input.strip().lower() in ("exit", "quit"):
            break
        if not user_input.strip():
            continue
        messages.append({"role": "user", "content": user_input})
        reply = run_agent(messages)
        print(f"\nAgent: {reply}")


if __name__ == "__main__":
    main()