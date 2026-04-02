# Format specifiers = {value:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)

# :(number) = allocate that many spaces

# :03 = allocate and zero pad that many spaces

# :<(number) = left justify

# :>(number) = right justify

# :^ = center align

# :+ = use a plus sign to indicate positive value

# := = place sign to leftmost position

# : = insert a space before positive numbers

# :, = comma seperator

price_1 = 3000.14159
price_2 = -9870.65
price_3 = 1200.34

print(f"Price 1 is ${price_1:+,.2f}")
print(f"Price 2 is ${price_2:+,}")
print(f"Price 3 is ${price_3:+,}")
