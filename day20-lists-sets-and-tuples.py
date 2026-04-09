# collection = single "variable" used to store many values

# List [] = ordered and mutable. Duplicates OK

# Set = {} unordered and immutable, but Add/remove OK. NO duplicates

# Tuple = () ordered and immutable. Duplicates OK. Faster

fruits = ["apple", "oranage", "banana", "coconut"]

# print("apple" in fruits) // This prints True

# print(len(fruits))

# print(fruits[::2])

# fruits[0] = "pineapple" // replaces apple with pineapple

# Adds pineapple at the END of the list
# fruits.append("pineapple")

# fruits.remove("apple")

# Adds pineapple at 0th index
# fruits.insert(0, "pineapple")

# Sorts the list in alphabetical order
# fruits.sort()

# fruits.reverse()

# Removes all the elements from the list
# fruits.clear()

# print(fruits.index("apple"))

# Counts how many times banana appears in list
# print(fruits.count("banana"))

# print(fruits)

# Sets

cars = {"bmw", "dodge", "bugati"}

# These appear in a different order when printed
# print(cars)

# print("bmw" in cars)
# print(len(cars))
# cars.add("mazdaa")
# cars.remove("mazda")
# pop, clear also work
# print(cars)

# Tuples

vegetables = ("Cauliflower", "Broccoli", "Radish")
# count, index, len, in operator and for loop method work
print(vegetables)
