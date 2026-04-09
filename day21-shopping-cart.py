foods = []
prices = []
total = 0

while True:
    food = input("Enter the food you want to eat (q/Q to exit): ")
    if not food.lower() == "q":
        foods.append(food)
        price = float(input(f"Enter the price of {food}: "))
        prices.append(price)
    else:
        break

print("-----YOUR CART------")

for food in foods:
    print(food, end=", ")

for price in prices:
    total += price

print(f"Your total is ${total:.2f}")
