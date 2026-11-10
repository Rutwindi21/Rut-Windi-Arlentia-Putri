class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Nama Restoran: {self.restaurant_name}")
        print(f"Jenis Masakan: {self.cuisine_type}")

class IceCreamStand(Restaurant):
    """Representasi khusus dari restoran es krim yang mewarisi dari Restaurant."""

    def __init__(self, restaurant_name, cuisine_type='Ice Cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Vanila', 'Cokelat', 'Stroberi', 'Mangga', 'Matcha']

    def display_flavors(self):
        """Menampilkan daftar rasa es krim yang tersedia."""
        print("Daftar rasa es krim yang tersedia:")
        for flavor in self.flavors:
            print(f"- {flavor}")

# Membuat instance dari IceCreamStand dan memanggil metodenya
my_ice_cream_stand = IceCreamStand("Gelato Paradise")
my_ice_cream_stand.describe_restaurant()
my_ice_cream_stand.display_flavors()