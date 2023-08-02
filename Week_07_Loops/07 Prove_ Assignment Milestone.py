#-07 Prove: Assignment Milestone
#-Wordle Program Demo

print('Welcome to the word guessing game!')
print("Let's play!")
print('-' * 35)

s_word = 'programming'
count = 0
guess = ''

size1 = len(s_word)


while guess != s_word:

  print('\nYour hint is: _ _ _ _ _ _ ')
  guess = input('What is your guess?') 
  size2 = len(guess)
  
  if size1 == size2:
    
    count += 1
    
    for i in range(s_word.__len__()):
      
            if guess[i] == s_word[i]:
                output = guess[i]
                print(output.upper(), end='')
              
            elif guess[i] in s_word:
                output = guess[i]
                print(output.lower(), end='')
              
            else:
                output = guess[i]
                print('_', end='')
                
    
    
  else:
    print('\nSorry, the guess must have the same number of letters as the secret word.')
    count += 1

print('\nCongratulations! You guessed it!')
print(f'It took you {count} guesses.')


