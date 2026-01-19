# Strings
first_name='Saad'
food='Biryani'
email='bro123@fake.com'

# Integers
age=21
quantity=3
num_of_students= 30

# Float
price = 10.99
gpa= 3.4

# Booleans
# !True and False first letter uppercase!
is_student = True
for_sale = False

# Using variables (python version of ${})
# Add f before "" and inside the quotation goes {variable_name}
print(f"Hello {first_name}")
print(f"You like {food}?")
print(f"Your email is {email}")
print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")
print(f"The price is ${price}")
print(f"Your GPA is {gpa}")
print(f"Are you a student?: {is_student}")

# No brackets for variable in if-else
if for_sale: 
  print('That item is for sale')
else:
  print('That item is not available')