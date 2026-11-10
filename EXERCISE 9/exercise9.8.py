class User:
    """Kelas dasar untuk menyimpan profil pengguna."""

    def __init__(self, first_name, last_name, age, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.username = username
        self.email = email

    def describe_user(self):
        print(f"\nProfil Pengguna: {self.username}")
        print(f"Nama Lengkap: {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Halo, {self.first_name}!")


class Privileges:
    """Kelas terpisah untuk menyimpan dan mengelola daftar hak istimewa."""

    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """Menampilkan daftar hak istimewa."""
        print("Daftar Hak Istimewa:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """Kelas Admin yang menggunakan kelas Privileges (Komposisi)."""

    def __init__(self, first_name, last_name, age, username, email):
        super().__init__(first_name, last_name, age, username, email)
        self.privileges = Privileges()


admin_2 = Admin("Stella", "Jung", 27, "stella_admin", "stella.admin@gmail.com")
admin_2.describe_user()
admin_2.privileges.show_privileges()