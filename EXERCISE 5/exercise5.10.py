current_users = ['feli', 'rachel', 'vega', 'sofia', 'admin']
new_users = ['RACHEL', 'rara', 'VEGA', 'vena', 'galih']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Nama pengguna '{new_user}' sudah digunakan. Silakan masukkan nama pengguna lain.")
    else:
        print(f"Nama pengguna '{new_user}' tersedia.")