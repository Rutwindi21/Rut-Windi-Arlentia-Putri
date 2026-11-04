usernames = ['admin', 'sofia', 'feli', 'vega', 'rachel']

for username in usernames:
    if username == 'admin':
        print("Halo admin, apakah Anda ingin melihat status laporannya?")
    else:
        print(f"Halo {username.title()}, terima kasih telah login kembali.")