# iterables = An object/collection that can return its elements one at a time, allowing it to be iterated over in a loop

# numbers = [1, 2, 3, 4, 5]

# for number in reversed(numbers):
#     print(number, end=" ")

# name = "Saad Hussain"

# for character in name:
#     print(character, end=" ")

my_dict = {"A": 1, "B": 2, "C": 3}

# method to print only keys
# for key in my_dict:
#     print(key)

# method to print only values
# for value in my_dict.values():
#     print(value)

for key, value in my_dict.items():
    print(f"{key}: {value}")
