# Sama dan tidak sama dengan string
buah = 'Apel'
print(buah == 'Apel')  # True
print(buah != 'Pisang') # True

# Menggunakan metode lower()
print(buah.lower() == 'apel') # True
print(buah.lower() == 'Apel') # False

# Tes numerik
umur = 20
print(umur == 20) # True
print(umur != 20) # False
print(umur > 15)  # True
print(umur < 15)  # False
print(umur >= 20) # True
print(umur <= 19) # False

# Kata kunci and dan or
print(umur > 18 and buah == 'Apel') # True
print(umur > 25 and buah == 'Apel') # False
print(umur > 25 or buah == 'Apel')  # True
print(umur < 18 or buah == 'Pisang') # False

# Memeriksa apakah item ada di dalam list
topping = ['jamur', 'bawang bombay', 'nanas']
print('jamur' in topping) # True
print('pepperoni' in topping) # False

# Memeriksa apakah item TIDAK ada di dalam list
user_terlalang = ['risa', 'sarah', 'nadia']
user = 'riri'
print(user not in user_terlalang) # True
print('andrew' not in user_terlalang) # False