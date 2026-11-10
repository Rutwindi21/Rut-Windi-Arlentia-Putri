class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 

    def describe_restaurant(self):
        print(f"Nama Restoran: {self.restaurant_name}")
        print(f"Jenis Masakan: {self.cuisine_type}")
        print(f"Jumlah Pelanggan yang Dilayani: {self.number_served}")

    def set_number_served(self, number):
        """Mengatur jumlah pelanggan yang telah dilayani."""
        self.number_served = number

    def increment_number_served(self, additional_customers):
        """Menambahkan jumlah pelanggan yang dilayani."""
        self.number_served += additional_customers

# Membuat instance dan mencetak nilai default
restaurant = Restaurant("Sederhana", "Masakan Padang")
print(f"Jumlah pelanggan awal: {restaurant.number_served}")

# Mengubah nilainya secara langsung dan mencetak ulang
restaurant.number_served = 15
print(f"Jumlah pelanggan setelah diubah langsung: {restaurant.number_served}")

# Menggunakan metode set_number_served
restaurant.set_number_served(50)
print(f"Jumlah pelanggan setelah menggunakan set_number_served: {restaurant.number_served}")

# Menggunakan metode increment_number_served
restaurant.increment_number_served(25)
print(f"Jumlah pelanggan setelah ditambah (increment): {restaurant.number_served}")