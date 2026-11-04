favorite_numbers = {
    'Rut': [7, 14, 21],
    'Kirania': [12, 99],
    'Djilva': [3],
    'Vani': [25, 100],
    'Kayla': [9, 18, 27]
}

for name, numbers in favorite_numbers.items():
    print(f"Angka favorit {name} adalah:")
    for number in numbers:
        print(f"  * {number}")
    print()