print("Masukkan dua angka untuk dijumlahkan.")
print("Ketik 'q' untuk keluar kapan saja.\n")

while True:
    first_number = input("\nAngka pertama: ")
    if first_number.lower() == 'q':
        break
        
    second_number = input("Angka kedua: ")
    if second_number.lower() == 'q':
        break

    try:
        # Mengubah input string menjadi integer
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Error: Mohon masukkan angka yang valid, bukan teks!")
    else:
        print(f"Hasil penjumlahannya adalah: {answer}")