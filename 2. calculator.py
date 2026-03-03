# Converting the strings into float/integers
# x = float(input('Enter x: '))
# y = float(input('Enter y: '))

# Rounds to the number if its .5 or more
# z = round(x+y)

# Adds comma for 1,000/1,000,000 etc.
# print(f"{z:,}")

# Rounds to 2 decimal places
# w = round(x/y, 2)
# print(w)

# Function that accepts 2 numbers and squares them
def main():
  x = int(input('Enter c: '))
  y = int(input('Enter d: '))
  print(f"{x} squared is {square(x)}")
  print(f"{y} squared is {square(y)}")
  
def square(value):
  return value ** 2

main()