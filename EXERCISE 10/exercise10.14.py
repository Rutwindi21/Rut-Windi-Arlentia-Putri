from pathlib import Path
import json

def get_stored_username(path):
  """Mengambil nama pengguna yang tersimpan jika ada."""
  if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    return username
  else:
    return None


def get_new_username(path):
  """Meminta nama pengguna baru dan menyimpannya."""
  username = input("Siapa nama Anda? ")
  contents = json.dumps(username)
  path.write_text(contents)
  return username


def greet_user():
  """Menyapa pengguna dengan verifikasi apakah itu benar dirinya."""
  path = Path("username.json")
  username = get_stored_username(path)

  if username:
    # Verifikasi apakah pengguna saat ini adalah pemilik data yang tersimpan[cite: 4]
    correct = input(f"Apakah nama Anda {username}? (y/n): ")
    if correct.lower() == "y":
      print(f"Selamat datang kembali, {username}!")
    else:
      username = get_new_username(path)
      print(f"Kami akan mengingat Anda saat Anda kembali, {username}!")
  else:
    username = get_new_username(path)
    print(f"Kami akan mengingat Anda saat Anda kembali, {username}!")


greet_user()