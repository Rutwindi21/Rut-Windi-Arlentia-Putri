rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'citarum': 'indonesia'
}

# 1. Loop mencetak kalimat tentang setiap sungai
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\n--- Nama Sungai ---")

# 2. Loop mencetak hanya nama sungai (keys)
for river in rivers.keys():
    print(river.title())

print("\n--- Nama Negara ---")

# 3. Loop mencetak hanya nama negara (values)
for country in rivers.values():
    print(country.title())