# Sistem Verifikasi Kelayakan Diskon Bioskop
# Ide: Membuat program sederhana yang memeriksa usia penonton 
# dan status keanggotaan untuk menentukan harga tiket bioskop.

usia = 20
punya_kartu_member = True

print("--- Sistem Pengecekan Diskon Tiket Bioskop ---")

if usia < 12:
    print("Tiket anak-anak: Harga Rp30.000")
elif usia >= 60:
    print("Tiket lansia: Harga Rp30.000")
elif punya_kartu_member:
    print("Diskon khusus member: Harga Rp35.000")
else:
    print("Tiket reguler: Harga Rp50.000")