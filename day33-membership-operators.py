# Membership operators = used to test whether a value is found in a sequence (string, list, tuple, set or dictionary)

# 1. in 2. not in

# word = "APPLE"

# letter = input("Guess a letter in the secret word: ")

# if letter in word:
#     print(f"There is a {letter}")
# else:
#     print(f"{letter} was not found")

# if not letter in word:
#     print(f"{letter} was not found")
# else:
#     print(f"There is a {letter}")

# students = ["Spongebob", "Patrick", "Sandy"]

# student = input("Enter student's name: ")

# if student in students:
#     print(f"{student} is present")
# else:
#     print(f"{student} does not exist")

# grades = {"Sandy": "A", "Pat": "B", "Sponge": "C"}

# student = input("Enter the name of a student: ")

# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f"{student} does not exist")

email = "saad@gmail.com"

if "@" in email and "." in email:
    print(f"Welcome {email}!")
else:
    print("Email is not valid")
