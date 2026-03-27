num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter the operation you want to do: ")

if operation == '+':
  result = num1 + num2
  print(round(result,2))
elif operation == '-':
  result = num1 - num2
  print(round(result,2))
elif operation == '*':
  result = num1 * num2
  print(round(result,2))
elif operation == '/':
  result = num1 / num2
  print(round(result,2))
else:
  print('Not a valid operation.')