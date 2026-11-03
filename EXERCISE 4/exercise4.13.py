menu_items = ('nasi goreng', 'ayam crispy', 'sop sayur', 'mie kuah', 'sate ayam')

print("Menu asli restoran:")
for item in menu_items:
    print(item)

# Percobaan mengubah item (akan memicu TypeError jika dijalankan)
# menu_items[0] = 'rendang'

# Restoran mengubah menu (menetapkan tuple baru ke variabel yang sama)
menu_items = ('nasi goreng', 'rendang sapi', 'sop sayur', 'ikan bakar', 'sate ayam')

print("\nMenu baru restoran setelah direvisi:")
for item in menu_items:
    print(item)