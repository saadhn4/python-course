# keyword arguments = an argument preceded by an identifier
# helps w readability
# order of arguments doesnt matter
# 1. positional 2. default 3. KEYWORD 4. arbitrary


def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")


# positional arguments should always be first, in this case the greeting

# notice how the arguments doesnt follow the order of the parameters
# hello("Hello", first="Patrick", last="Bob", title="Mr.")


def get_phone(country, area, first, last):
    return f"+{country}({area})-{first}-{last}"


phone_num = get_phone(country=1, first=456, last=789, area=123)

print(phone_num)
