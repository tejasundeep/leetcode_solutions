print("""
Pizza Sizes:
1. Small - Rs. 300
2. Medium - Rs. 500
3. Large - Rs. 700
""")

pizza_size = input("Enter the size of pizza?: ")
pizza_size = int(pizza_size)

pizza_price = 0
if pizza_size == 1:
    pizza_price += 300
elif pizza_size == 2:
    pizza_price += 500
elif pizza_size == 3:
    pizza_price += 700

print("""
Pizza Sizes:
1. Pepperoni - Rs. 25
2. Mushroom - Rs. 30
3. Extra cheese - Rs. 15
4. Sausage - Rs. 30
5. Onion - Rs. 15
6. Black olives - Rs. 35
7. Green pepper - Rs. 25
8. Fresh garlic - Rs. 10
""")

toppings_count = input("How many toppings you need?: ")

addons = {}
addon_price = [25, 30, 15, 30, 15, 35, 25, 10]
for i in range(int(toppings_count)):
    addon_items = input("Enter your toppings: ")
    addons[f'{i}'] = addon_price[i]



total = sum(addons.values()) + pizza_price
tax = total * 0.05
total = total + tax

print(f"""
Pizza Price: Rs. {pizza_price}
Topping Price: Rs. {sum(addons.values())}
Tax: Rs. {tax}
Total Price: Rs. {total}
""")