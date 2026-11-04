cities = {
    'surakarta': {
        'country': 'indonesia',
        'population': '522.000 jiwa',
        'fact': 'Dikenal sebagai pusat kebudayaan Jawa dan industri batik.',
        'landmarks': ['Keraton Surakarta', 'Pura Mangkunegaran', 'Pasar Triwindu']
    },
    'tokyo': {
        'country': 'jepang',
        'population': '13.960.000 jiwa',
        'fact': 'Kawasan metropolitan dengan populasi terpadat di dunia.',
        'landmarks': ['Tokyo Tower', 'Shibuya Crossing', 'Kiyomizu-dera']
    },
    'paris': {
        'country': 'prancis',
        'population': '2.160.000 jiwa',
        'fact': 'Terkenal dengan sebutan Kota Cahaya (City of Light).',
        'landmarks': ['Menara Eiffel', 'Museum Louvre', 'Katedral Notre-Dame']
    }
}

for city_name, city_info in cities.items():
    print(f"\n Informasi Kota: {city_name.title()}")
    print(f"   • Negara   : {city_info['country'].title()}")
    print(f"   • Populasi : {city_info['population']}")
    print(f"   • Fakta    : {city_info['fact']}")
    
    print(f"   • Landmark Terkenal:")
    for landmark in city_info['landmarks']:
        print(f"     - {landmark}")
        
    print("-" * 50)