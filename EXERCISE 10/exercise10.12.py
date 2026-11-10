from pathlib import Path
import json

path = Path("files/favorite_number.json")

if path.exists():
    contents = path.read_text()
    favorite_number = json.loads(contents)
    print(f"Saya tahu angka favorit Anda! Angkanya adalah {favorite_number}.")
else:
    number = input("Berapa angka favorit Anda? ")
    path.write_text(json.dumps(number))
    print("Kami akan mengingatnya lain kali!")