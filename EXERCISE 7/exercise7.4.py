prompt = "\nMasukkan toping pizza (ketik 'selesai' saat sudah selesai): "

while True:
    topping = input(prompt)
    if topping == 'selesai':
        break
    else:
        print(f"Saya akan menambahkan {topping} ke pizza anda!")