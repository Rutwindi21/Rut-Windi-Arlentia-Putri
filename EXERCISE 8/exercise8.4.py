def make_shirt(size="large", message="Home"):
    print(f"Membuat kaos ukuran {size} dengan cetakan teks: '{message}'.")

# Kaos large dengan pesan default
make_shirt()

# Kaos medium dengan pesan default
make_shirt(size="medium")

# Kaos ukuran apa saja dengan pesan berbeda
make_shirt(size="small", message="Teknik Industri!")