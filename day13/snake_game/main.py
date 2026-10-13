import os
import random
import time
import msvcrt  # 仅限 Windows

WIDTH, HEIGHT = 30, 15
DELAY = 0.15  # 每一步的间隔(秒),越小越快

DIRECTIONS = {"w": (0, -1), "s": (0, 1), "a": (-1, 0), "d": (1, 0)}
OPPOSITE = {"w": "s", "s": "w", "a": "d", "d": "a"}


def place_food(snake):
    """在没有被蛇占据的格子里随机放食物;没有空位返回 None。"""
    free = [(x, y) for x in range(WIDTH) for y in range(HEIGHT) if (x, y) not in snake]
    return random.choice(free) if free else None


def draw(snake, food, score):
    border = "+" + "-" * WIDTH + "+"
    lines = [border]
    for y in range(HEIGHT):
        row = ""
        for x in range(WIDTH):
            if (x, y) == snake[0]:
                row += "@"
            elif (x, y) in snake:
                row += "O"
            elif (x, y) == food:
                row += "*"
            else:
                row += " "
        lines.append("|" + row + "|")
    lines.append(border)
    lines.append(f"Score: {score}    W/A/S/D to move, Q to quit")
    print("\033[H" + "\n".join(lines))  # 光标回到左上角,避免闪烁


def main():
    os.system("")      # 让 Windows 终端支持 ANSI 转义序列
    os.system("cls")

    snake = [(WIDTH // 2, HEIGHT // 2)]  # 蛇身坐标列表,蛇头在最前面
    direction = "d"
    food = place_food(snake)
    score = 0

    while True:
        draw(snake, food, score)

        # 在一个时间片内读取按键(不阻塞)
        current = direction
        deadline = time.time() + DELAY
        while time.time() < deadline:
            if msvcrt.kbhit():
                key = msvcrt.getwch().lower()
                if key == "q":
                    print("Bye!")
                    return
                if key in DIRECTIONS and key != OPPOSITE[current]:
                    direction = key
            time.sleep(0.01)

        # 移动
        dx, dy = DIRECTIONS[direction]
        head = (snake[0][0] + dx, snake[0][1] + dy)

        # 撞墙或撞自己
        if not (0 <= head[0] < WIDTH and 0 <= head[1] < HEIGHT) or head in snake:
            draw(snake, food, score)
            print(f"Game Over! Final score: {score}")
            return

        snake.insert(0, head)
        if head == food:
            score += 1
            food = place_food(snake)
            if food is None:
                print("You win!")
                return
        else:
            snake.pop()



if __name__ == "__main__":
    main()