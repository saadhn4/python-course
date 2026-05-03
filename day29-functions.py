# function = A block of reusable code
# place () after the function name to invoke it


# def happy_birthday(name, age):
#     print(f"Happy birthday to {name}!")
#     print(f"You are {age} years old!")
#     print(f"Happy birthday to {name}!")
#     print()


# happy_birthday("Bro", 22)
# happy_birthday("Saad", 21)


# def display_invoice(uname, amt, ddate):
#     print(f"Hello {uname}")
#     print(f"Your bill of ${amt:.2f} is due: {ddate}")


# display_invoice("Saad", 42.5, "01/01")

# return = statement used to end a function
# and send a result back to the caller


# def add(a, b):
#     return a + b


# z = add(1, 2)
# print(z)


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last


full_name = create_name("saad", "hussain")
print(full_name)
