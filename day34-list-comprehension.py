# List comprehension = A concise way to create lists in python

# Compact and easier to read than traditional loops

# [expression for value in iterable if condition]

# Traditional way
# doubles = []

# for x in range(1, 11):
#     doubles.append(x * 2)

# doubles = [x * 2 for x in range(1, 11)]
# squared = [y**2 for y in range(1, 11)]

# print(squared)

# fruits = ["apple", "banana", "mango", "orange"]
# upper = [fruit.upper() for fruit in fruits]
# first_chars = [fruit[0] for fruit in fruits]

# print(upper)
# print(first_chars)

# numbers = [1, 2, 3, -2, -3, -5, 6]

# positive_nums = [number for number in numbers if number > 0]

# negative_nums = [number for number in numbers if number < 0]

# even_nums = [number for number in numbers if number % 2 == 0]

# print(positive_nums)
# print(negative_nums)
# print(even_nums)

# grades = [85, 42, 79, 90, 56, 61, 30]

# passing_grades = [grade for grade in grades if grade >= 60]

# print(passing_grades)
