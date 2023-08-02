#-07 Prepare: Preparation Material
#-Loops-While
'''
number = True

# Keep looping as long as the number is less than 10
while number:
    number = int(input("What is the number? "))

    if number <= 10:
      number = True
    
  
    else:
      number = False

if not number:
  case = True
  while case:
    name = input('What is your name?')
    print(f'Your name is {name}')

    if name == 'Jose Pablo':
      case = False 
'''
'''
# Start with the number 1
number = 1

# Keep looping as long as the number is less than or equal to 5
while number <= 5:
    # Display the number
    print(f"The number is: {number}")
    
    # Update the number to be one more than it was
    number += 1 

print("Finished with the loop")
'''
number = 0
name = ""

while number < 10: 
    number = int(input("What is the number? "))
    name = input("What is your name?")

print(f"Your name is: {name}")