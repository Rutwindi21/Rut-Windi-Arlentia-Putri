from random import randint

class Dice:
    """Kelas untuk merepresentasikan sebuah dadu."""

    def __init__(self, sides=6):
        """Inisialisasi jumlah sisi pada dadu (default 6 sisi)."""
        self.sides = sides

    def roll_dice(self):
        """Mengembalikan angka acak antara 1 dan jumlah sisi dadu."""
        return randint(1, self.sides)

# 1. Membuat dadu standar ber-sisi 6 dan melemparnya 10 kali
print("--- Lemparan Dadu Bermata 6 (10 kali) ---")
dadu_6 = Dice(6)
for _ in range(10):
    print(dadu_6.roll_dice(), end=" ")
print("\n")

# 2. Membuat dadu ber-sisi 10 dan melemparnya 10 kali
print("--- Lemparan Dadu Bermata 10 (10 kali) ---")
dadu_10 = Dice(10)
for _ in range(10):
    print(dadu_10.roll_dice(), end=" ")
print("\n")

# 3. Membuat dadu ber-sisi 20 dan melemparnya 10 kali
print("--- Lemparan Dadu Bermata 20 (10 kali) ---")
dadu_20 = Dice(20)
for _ in range(10):
    print(dadu_20.roll_dice(), end=" ")