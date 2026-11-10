from Exercise11.exercise1 import city_country

def test_city_country():
    """Apakah kota seperti 'santiago' dan 'chile' berfungsi dengan benar?"""
    formatted_name = city_country('santiago', 'chile')
    assert formatted_name == 'Santiago, Chile'