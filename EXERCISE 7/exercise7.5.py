prompt = "\nMasukkan usia anda (ketik 'selesai' saat sudah selesai): "

while True:
    age = input(prompt)
    if age == 'selesai':
        break
    
    age = int(age)
    if age < 3:
        print("Tiket anda gratis!")
    elif age <= 12:
        print("Tiket anda Rp.40.000,00.")
    else:
        print("Tiket anda Rp.55.000,00.")