# Compound interest calculatoe

principle = float(input("Enter principle: "))

while principle <= 0:
    print("Principle cannot be less than or equal to 0")
    principle = float(input("Enter principle: "))


rate = float(input("Enter rate: "))

while rate <= 0:
    print("Interest cannot be less than or equal to 0")
    rate = float(input("Enter rate: "))


time = float(input("Enter time in years: "))

while time <= 0:
    print("Time cannot be less than or equal to zero")
    time = float(input("Enter time: "))


total = principle * (1 + rate / 100) ** time
print(f"Balance after {time} years is ${total:.2f}")
