# Type casting - The process of converting a value of one data type to another (str, int, float, bool)
# Explicit vs Implicit

name = 'Saad'
age = 22
gpa = 3.2
student = True

print(type(name))

# Explicit conversion
age = float(age)
print(type(age)) #22.0

gpa = int(gpa)
print(gpa) #3

student = str(student)
print(student) # True, but now it's a string

# What if you were to convert a number thats not 1/0 to bool?
# Anything thats not 0 = true

age = bool(age)
print(age) #True

# Same with strings. If empty string -> false

# Implicit conversion
x = 2
y = 2.0

x = x/y

# Answer comes out in float
print(x)
