from pathlib import Path

path = Path("files/guest_book.txt")
guest_entries = ""

print("Ketik 'keluar' jika sudah selesai.")
while True:
    name = input("Masukkan nama Anda: ")
    if name.lower() == "keluar":
        break
    guest_entries += f"{name}\n"
    print(f"Halo {name}, kehadiran Anda telah dicatat.")

path.write_text(guest_entries)