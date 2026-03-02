# python file_name is the command to run the code

# Ask user for their name
# strip Removes whitespace from string (String method)
# title Capitalizes first letter of each word
# capitalize Only capitalizes first word
name = input("What's your name? ").strip().title()

# Split user's name into first and last name
# first is a variable that will store the first word
# last stores whatever user typed after the first word
# splits the string after every space
first,last = name.split(" ")

# Say hello to user
# f strings (f'blah blah {variable}')
print(f"Hello, {first}")