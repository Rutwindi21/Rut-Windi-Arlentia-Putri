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


class Admin(User):
    """Kelas khusus untuk pengguna dengan hak akses admin."""

    def __init__(self, first_name, last_name, age, username, email):
        super().__init__(first_name, last_name, age, username, email)
        self.privileges = ["can add post", "can delete post", "can ban user", "can moderate comments"]

    def show_privileges(self):
        """Menampilkan daftar hak istimewa admin."""
        print(f"Daftar Hak Istimewa Admin ({self.username}):")
        for privilege in self.privileges:
            print(f"- {privilege}")

# Membuat instance Admin dan menampilkan hak istimewanya
admin_baru = Admin("Chika", "Utomo", 25, "chika_admin", "admin@gmail.com")
admin_baru.describe_user()
admin_baru.show_privileges()