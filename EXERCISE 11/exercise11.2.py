from Exercise11.exercise2 import city_country

def test_city_country():
    """Menguji format kota dan negara dasar."""
    formatted_name = city_country('santiago', 'chile')
    assert formatted_name == 'Santiago, Chile'

def test_city_country_population():
    """Menguji apakah kita dapat menyertakan populasi."""
    formatted_name = city_country('santiago', 'chile', population=5000000)
    assert formatted_name == 'Santiago, Chile - population 5000000'