person1 = {'first_name': 'Rut', 'last_name': 'Windi', 'age': 18, 'city': 'Surakarta'}
person2 = {'first_name': 'Kirania', 'last_name': 'Kusuma', 'age': 20, 'city': 'Jakarta'}
person3 = {'first_name': 'Vani', 'last_name': 'Kentza', 'age': 19, 'city': 'Yogyakarta'}

people = [person1, person2, person3]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"Nama Lengkap: {full_name}")
    print(f"Usia        : {person['age']}")
    print(f"Kota        : {person['city']}\n")