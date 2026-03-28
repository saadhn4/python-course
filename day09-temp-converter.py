temp = int(input("Enter temperature: "))
unit = input("Enter unit (f/c): ")

if unit == "c":
    temp = temp * 1.8 + 32
    print(f"Temperature is {round(temp,2)}F")
elif unit == "f":
    temp = (temp - 32) / 1.8
    print(f"Temperature is {round(temp,2)}C")
else:
    print(f"{unit} is not a proper temperature unit")
