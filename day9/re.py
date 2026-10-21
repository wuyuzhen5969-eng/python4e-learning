import re

with open("day9/file.txt", "r") as f:
    text = f.read()
    re.findall(r"\bz\w*", text) #raw string
    re.findall(r"\bc\b\s*\w+", text)

