from pathlib import Path
import json

number = input("Berapa angka favorit Anda? ")

path = Path("favorite_number.json")
contents = json.dumps(number)
path.write_text(contents)

print("Angka favorit Anda telah disimpan!")