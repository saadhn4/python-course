# nested loop = A loop within another loop

# for x in range(1, 10):
#     # end is by default \n
#     print(x, end="")


# for x in range(3):
#     for y in range(1, 10):
#         print(y, end="")
# this print is basically adding a \n : so next part of the code beings at a new line (123456789)
#     print()

# Create a rectangle using the same code above with different symbols

# Accept number of rows as an input from the user

rows = int(input("Enter # of rows: "))
columns = int(input("Enter # of columns: "))
symbol = input("Enter the symbol you want to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()
