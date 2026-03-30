name = input("Enter your full name: ")
phone_number = input("Enter phone number: ")

# 1. Returns length of the string (includes spaces)
print(len(name))

# 2. Returns the position where space appears for the FIRST time in the string (starts with index 0)
print(name.find(" "))

# 3. Returns the position where space appears for the LAST time in the string (starts with index 0)
print(name.rfind(" "))

# 4. Capitalizes the first letter in a string
print(name.capitalize())

# 5. Converts string to uppercase
print(name.upper())

# 6. Prints True if the string is ONLY numerical
print(name.isdigit())

# 7. Prints True if string contains ONLY alphabets
# If string has a space itll print false
print(name.isalpha())

# 8. Prints number of times '-' appears in a string
print(phone_number.count("-"))

# 9. Replaces '-' with empty space
print(phone_number.replace("-", " "))

# Validate user input exercise
# 1. username is less than or equal to 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")

if len(username) > 12:
    print("Username cannot be more than 12 characters")
elif not username.find(" ") == -1:
    print("Username cannot contain a space")
elif not username.isalpha():
    print("Username cannot contain any numericals")
else:
    print(f"Welcome {username}")
