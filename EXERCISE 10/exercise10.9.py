from pathlib import Path

filenames = ["cats.txt", "dogs.txt"]

for filename in filenames:
    path = Path(filename)
    try:
        contents = path.read_text(encoding="utf-8")
        print(f"\n--- {filename} ---")
        print(contents)
    except FileNotFoundError:
        pass  # Gagal secara senyap tanpa menampilkan pesan error