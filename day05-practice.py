# 1. Type Casting Practice
# name = input('Enter name: ')
# age = int(input('Enter age: '))
# height = float(input('Enter height in cm: '))

# print(f"Hello {name}, You are {age} years old and {height}cm tall ")

# 2. Perimeter of rectangle
# length = float(input('Enter length: '))
# breadth = float(input('Enter breadth: '))
# perimeter = 2 * length * breadth
# print(f"The perimeter of the rectangle is {perimeter}")

# 3. Time Converter ⏱️
# seconds = int(input('Enter seconds: '))
# hours = seconds / 3600
# minutes = (seconds % 3600) / 60
# print(f'Hours: {hours} ')
# print(f"Minutes: {minutes}")

# 4. Shopping Cart Upgrade

# Take:

# item
# price
# quantity

# Print:

# total cost
# cost per item (after calculation)

item = input("Enter item's name: ")
price = float(input("Enter item's price: "))
quantity = int(input('Enter number of items: '))

total_cost = price * quantity 

print(f"The total cost of {quantity} {item} is ${total_cost}")
print(f"The price of 1 {item} is {price}")

# 5. Trip Cost Calculator
distance = int(input('How many km away is your destination: '))

distance_covered = int(input('How many km per liter:'))

price = int(input('Enter price of fuel: '))

liters_needed = distance / distance_covered
total_cost = price * liters_needed





