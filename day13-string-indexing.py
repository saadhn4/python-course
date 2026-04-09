# indexing = accessing elements of a sequence using []
# [start: end: step]

credit_number = "1234-5678-9012-3456"

print(credit_number[0])

# first 4 digits of a string
# this does not include the 5th element (aka on index 4)
print(credit_number[0:4])

# prints 5678
print(credit_number[5:9])

# prints every element of the string starting from the 5th index
print(credit_number[5:])

# prints element on the last index of the string
print(credit_number[-1])

# prints every second character of the string (gap of 1) (starts with 1 tho cuz we know if we leave start value empty its 0)
print(credit_number[::2])

# Get last 4 digits of a credit card number
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

# reverse the credit card number
print(credit_number[::-1])

# Email splicer exercise

email = "saad11fadis@gmail.com"

index = email.find("@")

username = email[0:index]

domain = email[index + 1 :]

print(f"The username is {username} and the domain is {domain}")
