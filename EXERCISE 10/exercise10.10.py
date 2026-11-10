from pathlib import Path


def count_words(filename, target_word):
  """Menghitung perkiraan kemunculan suatu kata di dalam file teks."""
  path = Path(filename)
  try:
    contents = path.read_text(encoding="utf-8")
  except FileNotFoundError:
    print(f"Maaf, file {filename} tidak dapat ditemukan.")
  else:
    # Menghitung berapa kali target_word muncul (menggunakan lower agar tidak case-sensitive)
    count = contents.lower().count(target_word)
    print(
        f"Kata '{target_word}' muncul sekitar {count} kali di dalam"
        f" {filename}."
    )


# Contoh daftar file teks yang akan dianalisis dan kata yang dicari
filenames = ["alice.txt", "siddhartha.txt", "moby_dick.txt"]
word_to_find = "the"

for filename in filenames:
  count_words(filename, word_to_find)