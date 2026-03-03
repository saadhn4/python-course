# python file_name is the command to run the code

# Ask user for their name
# strip Removes whitespace from string (String method)
# title Capitalizes first letter of each word
# capitalize Only capitalizes first word
# name = input("What's your name? ").strip().title()

# Split user's name into first and last name
# first is a variable that will store the first word
# last stores whatever user typed after the first word
# splits the string after every space
# first,last = name.split(" ")

# Say hello to user
# f strings (f'blah blah {variable}')
# print(f"Hello, {first}")

# Functions
# def -> define

# We have a main function with the main part of our code and then im simply calling the hello function inside it
def main():
 name = input('Enter your name: ')
 # Here name gets copied to the variable 'to'; whatever user entered
 hello(name)

# Accepts variable to with default value world
def hello(to="world"):
  print(f'Hello, {to}')

# Since the function here is called with no argument passed it just says hello world, since we assigned the default value of variable 'to' as world
# hello()

# Calling the main function
main()



  