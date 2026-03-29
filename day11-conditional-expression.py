# Conditional expression -> one line shortcut for if else
# Print or assign one of two values based on condition
# !!!!!! X if condition else Y !!!!!!!!
# Same as terenary operator

num = 5
print("Positive" if num > 0 else "Negative")
print("Even" if num % 2 == 0 else "Odd")

a = 6
b = 7
max_num = a if a > b else b
print(max_num)

age = 25
status = "Adult" if age >= 18 else "Child"
print(status)

temp = 30
weather = "Hot" if temp > 20 else "Cold"
print(weather)

user_role = "guest"
access_level = "Full access" if user_role == "admin" else "Limited access"
print(access_level)
