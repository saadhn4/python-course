# if = do some code only if some condition is true
#      else do something else

# 1.
age = int(input('Enter your age: '))


if age >= 100:
  print('You are too old to sign up')
elif age >= 18:
    print("You are now signed up")
elif age < 0:
  print('You havent been born yet')
else: 
  print("You must be 18+ to sign up")

# 2.
response = input('Would you like food? (Y/N): ')

if response == 'Y':
  print('Have some food!')
else : 
  print('No food for you!')

# 3.
name = input('Enter your name: ')

if name == '':
  print('PLEASE ENTER YOUR NAME!!!!')
else: 
  print(f'Hello {name}')

# 4.
for_sale = True

if for_sale:
  print('This item is for sale')
else:
  print('This item is NOT for sale')