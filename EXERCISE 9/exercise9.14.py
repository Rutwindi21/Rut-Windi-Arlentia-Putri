from random import choice

# Membuat daftar berisi 10 angka dan 5 huruf
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

print("--- Undian Lotere Hari Ini ---")
winning_ticket = []

# Memilih 4 item secara acak tanpa duplikasi langsung (menggunakan perulangan)
while len(winning_ticket) < 4:
    pulled_item = choice(lottery_pool)
    if pulled_item not in winning_ticket:
        winning_ticket.append(pulled_item)

print(f"Tiket yang cocok dengan kombinasi berikut dinyatakan menang: {winning_ticket}")