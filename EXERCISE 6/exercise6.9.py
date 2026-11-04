favorite_places = {
    'Rut': ['Surakarta', 'Yogyakarta', 'Bali'],
    'Kirania': ['Bandung', 'Malang'],
    'Vani': ['Lombok']
}

for name, places in favorite_places.items():
    print(f"Tempat favorit {name}:")
    for place in places:
        print(f"- {place}")
    print()