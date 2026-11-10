class User:
    """Kelas untuk menyimpan profil pengguna."""

    def __init__(self, first_name, last_name, age, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.username = username
        self.email = email

    def describe_user(self):
        """Mencetak ringkasan informasi pengguna."""
        print(f"\nProfil Pengguna: {self.username}")
        print(f"Nama Lengkap: {self.first_name} {self.last_name}")
        print(f"Usia: {self.age} tahun")
        print(f"Email: {self.email}")

    def greet_user(self):
        """Memberikan sapaan personal kepada pengguna."""
        print(f"Halo, {self.first_name}! Selamat datang kembali di sistem.")

user1 = User("Rut", "Windi", 18, "rut_w", "rutwin@gmail.com")
user2 = User("Kim", "Ming", 19, "kim_m", "kiming@gmail.com")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()