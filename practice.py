# Practicing string methods

# 🧠 Exercise: Email Validator

# Write a program that asks the user for an email and checks the following:

# ✅ Rules:
# Email must be less than or equal to 20 characters
# Email must not contain spaces
# Email must contain exactly one "@"
# Email must end with ".com"
# Email should not be only numbers

# email = input("Enter your new email: ")

# if len(email) > 20:
#     print("Your email must be less than or equal to 20 characters")
# elif not email.find(" ") == -1:
#     print("Email cannot contain spaces")
# elif email.count("@") != 1:
#     print("Email can contain only one @")
# elif not email.endswith(".com"):
#     print("Email must end with .com")
# elif email.isdigit():
#     print("Email must not only be numerals")
# else:
#     print(f"Hi {email}")

# While loop

# 1. Password Check

# Ask the user to enter a password.
# Keep asking until the password is at least 6 characters long.

# password = input("Enter your password (atleast 6 characters): ")

# while len(password) < 6:
#     print("Password's length is too short")
#     password = input("Enter another password: ")

# print(f"Your password is {password}")

# 2. Positive Number Only

# Ask for a number.
# Keep asking until the number is greater than 0.

# num = int(input("Enter a number greather than 0: "))

# while num <= 0:
#     print(f"{num} is less than 0")
#     num = int(input("Enter a number greather than 0: "))

# print(f"Your number is {num}")

# 3. No Spaces Allowed

# Ask for a username.
# Keep asking if it contains a space.

# username = input("Enter a username: ")

# while not username.find(" ") == -1:
#     print("Username cannot contain spaces")
#     username = input("Enter another username: ")

# print(f"Your username is: {username}")

# 4. Valid Email Input

# Ask for an email until:

# No spaces
# Contains exactly one @
# Ends with .com

# email = input("Enter an email: ")

# while not email.find(" ") == -1 or email.count("@") != 1 or not email.endswith(".com"):
#     print(
#         "Email must not contain spaces or more than 1 @ and cannot end with anything other than .com"
#     )
#     email = input("Enter another email: ")

# print(f"Your email is {email}")

# Compound interest calculator
# Calculate the final amount
# Ask user for initial money(principle), interest rate and time in years

# principle = float(input("Enter principle: "))

# while principle <= 0:
#     print("Principle cannot be less than or equal to 0")
#     principle = float(input("Enter principle: "))


# rate = float(input("Enter rate: "))

# while rate <= 0:
#     print("Interest cannot be less than or equal to 0")
#     rate = float(input("Enter rate: "))


# time = float(input("Enter time in years: "))
# while time <= 0:
#     print("Time cannot be less than or equal to zero")
#     time = float(input("Enter time: "))


# total = principle * (1 + rate / 100) ** time
# print(f"Balance after {time} years is ${total:.2f}")

# 🧩 Exercise: ATM Withdrawal System
# 🎯 Task

# Create a program that simulates an ATM.

# 📌 Requirements
# Ask the user for:
# Account balance
# Withdrawal amount
# Validate inputs:
# Balance must be > 0
# Withdrawal must be > 0
# Withdrawal cannot exceed balance
# Keep asking until valid input is given.
# After valid input:
# Deduct withdrawal from balance
# Show remaining balance

acc_balance = float(input("Enter your bank balance: "))


while acc_balance <= 0:
    print("Balance cannot be less than 0")
    acc_balance = float(input("Enter your bank balance: "))

withdrawl = float(input("Enter the amount you want to withdraw: "))

while withdrawl <= 0:
    print("Amount withdrawn must be greater than zero")
    withdrawl = float(input("Enter the amount you want to withdraw: "))

while withdrawl > acc_balance:
    print("Cannot withdraw more than your balance")
    withdrawl = float(input("Enter the amount you want to withdraw: "))

new_balance = acc_balance - withdrawl
print(f"Your new balance is {new_balance}")
