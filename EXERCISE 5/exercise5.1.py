car = 'subaru'

print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("\n--- 5 Tes Evaluasi True ---")
print(car.lower() == 'subaru')
print(len(car) == 6)
print(car != 'toyota')
print(car.startswith('s'))
print('u' in car)

print("\n--- 5 Tes Evaluasi False ---")
print(car == 'Subaru') 
print(car == 'bmw')
print(len(car) > 10)
print(car.endswith('x'))
print('z' in car)