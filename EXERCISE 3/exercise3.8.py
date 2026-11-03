tempat = ['jepang', 'swiss', 'korea', 'paris', 'china']

print("Urutan asli:", tempat)

print("Urutan sorted:", sorted(tempat))

print("Urutan asli:", tempat)

print("Urutan sorted terbalik:", sorted(tempat, reverse=True))

print("Urutan asli:", tempat)

tempat.reverse()
print("Setelah reverse:", tempat)

tempat.reverse()
print("Urutan asli:", tempat)

tempat.sort()
print("Setelah sort:", tempat)

tempat.sort(reverse=True)
print("Sort reverse:", tempat)