from pathlib import Path

path = Path("files/learning_python.txt")

print("--- 1. Membaca seluruh file sekaligus ---")
contents = path.read_text()
print(contents)

print("--- 2. Melakukan perulangan langsung pada baris file ---")
lines = path.read_text().splitlines()
for line in lines:
    print(line)

print("--- 3. Menyimpan baris-baris ke dalam list dan melakukan perulangan ---")
for line in lines:
    print(line)