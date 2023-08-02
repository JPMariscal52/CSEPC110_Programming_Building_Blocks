#-07 Teach: Team Activity
#-Guess My Number Game

import random

guesses_number = 0

while True:
  
  number = random.randint(1, 100)

  print(f'Game {guesses_number}')
  
  trys = 0
  
  print('\nWhat is the magic number?')
  guess = -1
  
  while guess != number:
    
    print(f'Number of guesses {trys}')
    guess = int(input('What is your guess? '))

    
    if guess < number:
      print('Higher')
      trys += 1
  
    elif guess > number:
      print('Lower')
      trys += 1
      
    else:
      print('You guess it')
      

  answer = input('Do you want to keep playing (yes/no)? ')
  if answer == 'yes':
    guesses_number += 1
    continue

  else:
    print('Thank you for playing')
    break
    
    
