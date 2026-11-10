from pathlib import Path

path = Path("files/learning_python.txt")

for line in path.read_text().splitlines():
    print(line.replace("Python", "C"))