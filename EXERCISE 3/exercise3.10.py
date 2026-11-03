bahasa = ['Jawa', 'Sunda', 'Madura', 'Minang', 'Bali']

# 1. Mengakses elemen menggunakan indeks
print(f"Bahasa daerah pertama di list: {bahasa[0]}")

# 2. Mengubah elemen di dalam list
bahasa[0] = 'Bugis'
print("Setelah diubah:", bahasa)

# 3. Menambahkan elemen dengan append
bahasa.append('Batak')
print("Setelah append:", bahasa)

# 4. Menambahkan elemen dengan insert
bahasa.insert(1, 'Banjar')
print("Setelah insert:", bahasa)

# 5. Menghapus elemen dengan del
del bahasa[3]
print("Setelah del:", bahasa)

# 6. Menghapus elemen dengan pop
popped_bahasa = bahasa.pop()
print(f"Bahasa yang dihapus dengan pop: {popped_bahasa}")
print("List sekarang:", bahasa)

# 7. Menghapus elemen berdasarkan nilai dengan remove
bahasa.remove('Sunda')
print("Setelah remove('Sunda'):", bahasa)

# 8. Menyortir sementara dengan sorted
print("Urutan sorted:", sorted(bahasa))

# 9. Menyortir permanen dengan sort
bahasa.sort()
print("Setelah sort:", bahasa)

# 10. Membalik urutan secara permanen dengan reverse
bahasa.reverse()
print("Setelah reverse:", bahasa)

# 11. Menghitung panjang list dengan len
print(f"Jumlah bahasa yang tersisa: {len(bahasa)}")