# Practicing string methods

# 🧠 Exercise: Email Validator

# Write a program that asks the user for an email and checks the following:

# ✅ Rules:
# Email must be less than or equal to 20 characters
# Email must not contain spaces
# Email must contain exactly one "@"
# Email must end with ".com"
# Email should not be only numbers

email = input("Enter your new email: ")

if len(email) > 20:
    print("Your email must be less than or equal to 20 characters")
elif not email.find(" ") == -1:
    print("Email cannot contain spaces")
elif email.count("@") != 1:
    print("Email can contain only one @")
elif not email.endswith(".com"):
    print("Email must end with .com")
elif email.isdigit():
    print("Email must not only be numerals")
else:
    print(f"Hi {email}")
