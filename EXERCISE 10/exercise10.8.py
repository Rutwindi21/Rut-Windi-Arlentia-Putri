from pathlib import Path

filenames = ["cats.txt", "dogs.txt"]

for filename in filenames:
    path = Path(filename)
    print(f"\n--- Membaca file: {filename} ---")
    try:
        contents = path.read_text(encoding="utf-8")
        print(contents)
    except FileNotFoundError:
        print(f"Maaf, file {filename} tidak dapat ditemukan.")