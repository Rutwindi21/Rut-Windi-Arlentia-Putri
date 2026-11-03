list_tamu_undangan = ['Ren', 'Kirania', 'Tea', 'Nayla', 'Kala', 'Fadlila', 'Lana']

print("Mohon maaf teman-teman, ternyata meja sebelumnya masih belum siap. Aku hanya bisa mengundang beberapa orang saja.\n")

while len(list_tamu_undangan) > 2:
    tamu_dibatalkan = list_tamu_undangan.pop()
    print(f"Maaf {tamu_dibatalkan}, aku terpaksa membatalkan undangan makan malamnya.")

print("\n")

print(f"Haii {list_tamu_undangan[0]}, kamu tetap diundang untuk makan malam nanti ya.")
print(f"Haii {list_tamu_undangan[1]}, kamu tetap diundang untuk makan malam nanti ya.")

del list_tamu_undangan[0]
del list_tamu_undangan[0]

print("List tamu saat ini:", list_tamu_undangan)