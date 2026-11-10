class Battery:
    """Upaya sederhana untuk memodelkan baterai mobil listrik."""

    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Mobil ini memiliki baterai berkapasitas {self.battery_size}-kWh.")

    def get_range(self):
        if self.battery_size == 40:
            range_km = 150
        elif self.battery_size == 65:
            range_km = 220
        print(f"Mobil ini dapat menempuh jarak sekitar {range_km} mil dengan sekali pengisian daya.")

    def upgrade_battery(self):
        """Memeriksa kapasitas baterai dan meningkatkannya jika belum 65."""
        if self.battery_size != 65:
            self.battery_size = 65
            print("Baterai telah ditingkatkan menjadi 65-kWh.")
        else:
            print("Baterai sudah memiliki kapasitas maksimal.")


class ElectricCar:
    """Representasi sederhana dari mobil listrik."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.battery = Battery()

my_ev = ElectricCar('nissan', 'leaf', 2024)
my_ev.battery.describe_battery()
my_ev.battery.get_range()

print("\nMelakukan upgrade baterai...")
my_ev.battery.upgrade_battery()
my_ev.battery.describe_battery()
my_ev.battery.get_range()