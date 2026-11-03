list_tamu_undangan = ['Kirania', 'Nayla', 'Kala', 'Fadlila']

print("Haloo, ada informasi terbaru nih. Untuk acara nanti malam kita akan duduk di meja yang kapasitasnya lebih besar.\n")

list_tamu_undangan.insert(0, 'Ren')
list_tamu_undangan.insert(2, 'Tea')
list_tamu_undangan.append('Lana')

for tamu_undangan in list_tamu_undangan:
    print(f"Haii {tamu_undangan}, kamu diundang dalam acara makan malam di Resto Kusuma Sari nanti malam ya! Jangan lupa datang!")