# Typecasting is the process of converting a variable from one data type to another
# str(), int(), float(), bool()

name= 'Saad Hussain'
age= 22
gpa = 3.4
is_Student= True

print(type(name)) #<class 'str'>
print(type(age)) #<class 'int'>
print(type(gpa)) #<class 'float'>
print(type(is_Student)) #<class 'bool'>

# float to int
gpa = int(gpa)
print(gpa) #3

# int to float
age = float(age)
print(age) #22.0

# number to string
age = str(age)
print(type(age))

# string to boolean
name = bool(name)
print(name) # Since name is not an empty string, its True
print (type(name))