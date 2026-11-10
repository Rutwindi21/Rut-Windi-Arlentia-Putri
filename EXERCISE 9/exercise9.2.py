class Restaurant:
    """Sebuah kelas sederhana untuk merepresentasikan restoran."""

    def __init__(self, restaurant_name, cuisine_type):
        """Inisialisasi atribut restaurant_name dan cuisine_type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Mencetak informasi mengenai restoran."""
        print(f"Nama Restoran: {self.restaurant_name}")
        print(f"Jenis Masakan: {self.cuisine_type}")

    def open_restaurant(self):
        """Mencetak pesan bahwa restoran sedang buka."""
        print(f"{self.restaurant_name} saat ini sedang buka!")

restaurant = Restaurant("Sederhana", "Masakan Padang")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

restoran_1 = Restaurant("Soto Banjar Nyaman", "Kuliner Tradisional")
restoran_2 = Restaurant("Pizza Corner", "Fast Food")
restoran_3 = Restaurant("Sushi Ken", "Masakan Jepang")

print("\n")
restoran_1.describe_restaurant()
print("\n")
restoran_2.describe_restaurant()
print("\n")
restoran_3.describe_restaurant()