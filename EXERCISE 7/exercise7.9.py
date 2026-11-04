sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'salmon', 'pastrami', 'roast beef']
finished_sandwiches = []

print("Mohon maaf, toko kami kehabisan pastrami.\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"Aku membuat {current_sandwich} sandwich milikmu.")
    finished_sandwiches.append(current_sandwich)

print("\nList sandwich yang sudah selesai dibuat:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()}")