from pathlib import Path

path = Path("files/learning_python.txt")
lines = path.read_text().splitlines()

# Melakukan perulangan untuk setiap baris dan mengganti kata 'Python' dengan 'C'
for line in lines:
    modified_line = line.replace("Python", "C")
    print(modified_line)