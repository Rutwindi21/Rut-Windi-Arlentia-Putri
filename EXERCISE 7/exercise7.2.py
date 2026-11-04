group_size = input("Untuk berapa orang yang makan hari ini? ")
group_size = int(group_size)

if group_size > 8:
    print("Mohon maaf, kita harus waiting list terlebih dahulu.")
else:
    print("Meja anda sudah siap!")