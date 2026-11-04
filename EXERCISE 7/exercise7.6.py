print("Pilih Metode Kontrol Loop:")
print("1. Menggunakan Tes Kondisi (While condition)")
print("2. Menggunakan Variabel Active (Flag)")
print("3. Menggunakan Pernyataan Break")

pilihan = input("Masukkan pilihan Anda (1/2/3): ")
prompt = "\nMasukkan toping pizza (atau ketik 'selesai' untuk berhenti): "

if pilihan == '1':
    print("\n--- Menjalankan Versi 1: Kondisi While ---")
    topping = ""
    while topping != 'selesai':
        topping = input(prompt)
        if topping != 'selesai':
            print(f"Menambahkan {topping}!")

elif pilihan == '2':
    print("\n--- Menjalankan Versi 2: Variabel Active ---")
    active = True
    while active:
        topping = input(prompt)
        if topping == 'selesai':
            active = False
        else:
            print(f"Menambahkan {topping}!")

elif pilihan == '3':
    print("\n--- Menjalankan Versi 3: Pernyataan Break ---")
    while True:
        topping = input(prompt)
        if topping.strip() == 'selesai':
            break
        print(f"Menambahkan {topping}!")

else:
    print("Pilihan tidak valid. Silakan jalankan ulang program.")

print("\nProgram selesai. Terima kasih!")