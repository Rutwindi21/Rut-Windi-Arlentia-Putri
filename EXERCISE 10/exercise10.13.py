from pathlib import Path
import json

def get_stored_user_data(path):
  """Mengambil data pengguna yang tersimpan jika filenya ada."""
  if path.exists():
    contents = path.read_text()
    user_data = json.loads(contents)
    return user_data
  else:
    return None


def get_new_user_data(path):
  """Meminta informasi baru dari pengguna dan menyimpannya."""
  user_data = {}
  user_data["username"] = input("Siapa nama Anda? ")
  user_data["age"] = input("Berapa umur Anda? ")
  user_data["hobby"] = input("Apa hobi utama Anda? ")

  contents = json.dumps(user_data)
  path.write_text(contents)
  return user_data


def greet_user():
  """Menyapa pengguna berdasarkan data yang tersimpan."""
  path = Path("user_profile.json")
  user_data = get_stored_user_data(path)

  if user_data:
    print(f"Selamat datang kembali, {user_data['username']}!")
    print(f"Berikut adalah informasi yang kami ingat tentang Anda:")
    print(f"- Umur: {user_data['age']} tahun")
    print(f"- Hobi: {user_data['hobby']}")
  else:
    user_data = get_new_user_data(path)
    print(
        f"Kami akan mengingat Anda saat Anda kembali, {user_data['username']}!"
    )


greet_user()