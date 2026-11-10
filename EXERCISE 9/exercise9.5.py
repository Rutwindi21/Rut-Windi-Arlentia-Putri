class User:
    def __init__(self, first_name, last_name, age, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.username = username
        self.email = email
        self.login_attempts = 0 

    def describe_user(self):
        print(f"\nProfil Pengguna: {self.username}")
        print(f"Nama Lengkap: {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Halo, {self.first_name}!")

    def increment_login_attempts(self):
        """Menambahkan nilai login_attempts sebanyak 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Mereset nilai login_attempts menjadi 0."""
        self.login_attempts = 0

user = User("Marlo", "Hartono", 25, "marlo_h", "marlo@gmail.com")

# Memanggil increment_login_attempts beberapa kali
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Jumlah percobaan login: {user.login_attempts}")

# Mereset login attempts
user.reset_login_attempts()
print(f"Jumlah percobaan login setelah di-reset: {user.login_attempts}")