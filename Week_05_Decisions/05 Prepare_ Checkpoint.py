#-05 Prepare: Checkpoint
#-Practicing If Statements 
a = int(input('What is the first number? '))
b = int(input('What is the second number? '))

if a > b :
  print('The first number is greater')
else: 
  print('The first number is not greater')

if a == b :
  print('The numbers are equal')
else: 
  print('The numbers are not equal')
  
if a < b :
  print('The second number is greater')
else: 
  print('The second number is not greater')
print()

animal = input('What is your favorite animal? ')
if animal.lower() == 'duck':
  print("That's my favorite animal too!")
else:
  print("That one is not my favorite.")
  