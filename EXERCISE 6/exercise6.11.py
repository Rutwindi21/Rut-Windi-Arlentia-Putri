cities = {
    'Surakarta': {
        'country': 'Indonesia',
        'population': '522.000',
        'fact': 'Dikenal sebagai pusat kebudayaan Jawa dan batik.'
    },
    'Tokyo': {
        'country': 'Jepang',
        'population': '13.960.000',
        'fact': 'Kawasan metropolitan terbesar di dunia.'
    },
    'Paris': {
        'country': 'Prancis',
        'population': '2.160.000',
        'fact': 'Terkenal dengan sebutan Kota Cahaya (City of Light).'
    }
}

for city, info in cities.items():
    print(f"Kota: {city}")
    print(f"  Negara   : {info['country']}")
    print(f"  Populasi : {info['population']}")
    print(f"  Fakta    : {info['fact']}\n")