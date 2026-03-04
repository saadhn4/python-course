# str = input('Enter something: ')
# print(str.replace(':)','😀').replace(':(','🙁'))

def main():
  str= input('Enter text: ')
  print(convert(str))

def convert(string):
  return string.replace(':)','😀').replace(':(','🙁')
  
main()

