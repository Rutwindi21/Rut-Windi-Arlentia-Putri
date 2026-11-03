angka = [10, 20, 30]

# --- MEMBUAT INDEX ERROR ---
# List di atas hanya memiliki indeks 0, 1, dan 2. 
# Jika memanggil indeks 3, Python akan memunculkan IndexError.
# print(angka[3]) 

# --- CARA MEMPERBAIKINYA ---
# Ubah indeks ke rentang yang valid (0, 1, atau 2)
print("Nilai yang benar:", angka[2])