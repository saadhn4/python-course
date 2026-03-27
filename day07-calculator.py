num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))
operation = input("Enter the operation you want to do: ")

if operation == '+':
  result = num_1 + num_2
  print(round(result,2))
elif operation == '-':
  result = num_1 - num_2
  print(round(result,2))
elif operation == '*':
  result = num_1 * num_2
  print(round(result,2))
elif operation == '/':
  result = num_1 / num_2
  print(round(result,2))
else:
  print('Not a valid operation.')