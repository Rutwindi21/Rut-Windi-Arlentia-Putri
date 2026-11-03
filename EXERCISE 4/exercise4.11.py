my_pizzas = ['pepperoni', 'meat lovers', 'cheese']
friend_pizzas = my_pizzas[:]

my_pizzas.append('supreme')
friend_pizzas.append('mushroom')

print("Pizza favorit saya adalah:")
for pizza in my_pizzas:
    print(pizza)

print("\nPizza favorit teman saya adalah:")
for pizza in friend_pizzas:
    print(pizza)