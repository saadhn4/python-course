name = input('Enter your name: ')
age = int(input('Enter your age: '))

age = age + 1

print(f'Hello {name}')
print('Happy birthday!')
print(f"You are {age} years old")

# Ex 1. Calculate Area Of Rectangle

length = float(input('Enter length of rectangle: '))
breadth = float(input('Enter breadth of rectangle: '))
print(f"The area is: {length * breadth}cm^2")

# Ex 2. Shopping Cart Program

item = input('What item would you like to buy: ')
price = float(input("What is the price: "))
quantity = int(input('How many would you like: '))
total = price * quantity

print(f"You have bought {quantity} {item}/s")
print(f"Your total is ${total}")