import math

# Basic math operations
friends = 10
friends = friends + 1
friends += 1
friends -= 2
friends *= 3
friends /= 2
friends **= 2
friends %= 2

print(friends)

# Math related functions
# x = 3.14
# y = 4
# z = 5

# result = round(x) -> 3
# result = abs(y) -> if -4, itll be 4
# result = pow(4,3) -> 4x4x4
# result = max(x,y,z) -> 5
# result = min(x,y,z) -> 3.14

# print(result)

# Using math library
# print(math.pi)
# result = math.sqrt(4) square root of 4 is 2.0
# result = math.ceil(9.1) -> 10 (ceil rounds number up)
# result = math.floor(9.5) -> 9 (floor rounds number down)

# print(result)

# Exercises
# 1. Calculate circumference of a circle
radius = float(input('Enter radius: '))
circumference = 2 * math.pi * radius

# Rounding circumference to 2 digits
print(f"The circumference is {round(circumference, 2)}cm")

# 2. Calculate area of circle
r = float(input('Enter radius: '))
area = math.pi * pow(r,2)
print(f"The area of a circle is {round(area, 2)}cm")

# 3. Calculate hypotenuse of a right triangle
a = float(input('Enter a: '))
b = float(input('Enter b: '))
hypotenuse = math.sqrt(pow(a,2) + pow(b,2))

print(f'The hypotenuse of a right triangle is {round(hypotenuse, 2)}')
