responses = {}
polling_active = True

while polling_active:
    name = input("\nSiapa namamu? ")
    destination = input("Kalau kamu bisa pergi ke suatu tempat, kemana kamu akan pergi? ")
    
    responses[name] = destination
    
    repeat = input("Apakah kamu bersedia jika ada orang lain yang bergabung? (ya/tidak) ")
    if repeat == 'tidak':
        polling_active = False

print("\n--- Hasil Polling ---")
for name, place in responses.items():
    print(f"{name.title()} ingin mengunjungi {place.title()}.")