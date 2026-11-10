print("Masukkan dua angka untuk dijumlahkan.")
print("Ketik 'q' untuk keluar.")

while True:
    first_number = input("\nAngka pertama: ")
    if first_number == "q":
        break
    second_number = input("Angka kedua: ")
    if second_number == "q":
        break

    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Error: Mohon masukkan angka yang valid, bukan teks!")
    else:
        print(f"Hasil penjumlahannya adalah: {answer}")