weight = float(input('Enter weight: '))
unit = input('Enter unit of measurement (kg/lbs): ')

if unit == 'kg':
  weight *= 2.20462
  print(f"Your weight is {round(weight,2)}lbs")
elif unit == 'lbs':
  weight /= 2.20462
  print(f"Your weight is {round(weight,2)}kg")
else:
  print(f"{unit} is not a proper unit of measurement")
