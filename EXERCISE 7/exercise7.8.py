sandwich_orders = ['tuna', 'salmon', 'grilled cheese', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"Aku membuat {current_sandwich} sandwich milikmu.")
    finished_sandwiches.append(current_sandwich)

print("\nList sandwich yang sudah selesai dibuat:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()}")