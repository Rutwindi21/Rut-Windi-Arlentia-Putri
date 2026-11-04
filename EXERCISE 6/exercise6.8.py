pet1 = {'animal': 'Anjing', 'owner': 'Rut'}
pet2 = {'animal': 'Kelinci', 'owner': 'Kirania'}
pet3 = {'animal': 'Harimau', 'owner': 'Vani'}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"Jenis Hewan : {pet['animal']}")
    print(f"Pemilik     : {pet['owner']}\n")