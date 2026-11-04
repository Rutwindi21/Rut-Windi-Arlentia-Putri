favorite_languages = {
    'rut': 'python',
    'kirania': 'c',
    'ken': 'rust',
    'djilva': 'python',
}

people_to_poll = ['rut', 'kay', 'ken', 'desy', 'djilva', 'vrysa']

for person in people_to_poll:
    if person in favorite_languages:
        print(f"Terima kasih {person.title()} telah berpartisipasi dalam polling!")
    else:
        print(f"Halo {person.title()}, luangkan waktu sebentar untuk mengisi polling bahasa kesukaanmu!")