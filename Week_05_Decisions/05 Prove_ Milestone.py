#-05 Prove: Milestone
#-Adventure Game 

print('It is a beatiful night, you are cooking the dinner for your family, you go to your bedroom because you left your cellphone there and you want to check your text messages, when you come back you see that the oven is burning')

print('\nWhat are you going to do?')
print('Are you going to PUT out the fire by yourself, GO out for help, CALL to superman or PRAY for a miracle ?')

option = input('\nEnter an option(PUT/GO/CALL/PRAY): ')

option = option.lower()

#-First scenario
if option == 'put':
  print('\nAt that moment you remember that you can put out the fire using a FIRE extinguisher but this is in the garage, the WATER hose but it is in the yard or ASKING the oven to turn off.')
  choice = input('\nEnter your choice(FIRE/WATER/ASKING): ')
  choice = choice.lower()
  if choice == 'fire':
    print('\nYou run fast to the garage to bring the fire extinguisher, but you realize that your family forgot to recharge it, at that moment you see the valve gas next to the extinguisher and close it. When you come to the kitchen the fire has been put out')
  elif choice == 'water':
    print('\nYou go out to the yard for the water hose, open the faucet and turn off easily the fire')
  elif choice == 'asking':
    print('\nYou decided to ask the oven to turn off but this seems not to listen because the fire is rising, go away from there! ')
  else:
    print('\nYou are late, you could escape but your home is totally burned')

#-Second scenario
elif option == 'go':
  print('\nImmediately you go out and think what is better, ask for help with your NEIGHBOR quikly or go to BOMBER station, you have to chose right now!')
  choice = input('\nEnter your chose (NEIGHBOR/BOMBER): ')
  choice = choice.lower()
  if choice == 'neighbor':
    print('\nYou know that you do not have time and run with your neigbor, so you arrive to his house and nock the door, he comes out and see the smoke coming from your home, for your good luck, he had necesary equipment to put out the fire, you have saved your home!')
  elif choice == 'bomber':
    print('\nYou know the bomber station has the necesary equipment to put out the fire but it takes you 5 minutes go there, you decides run fast to arrive there and ask for help, the fireguards go to your home and put out the fire but the kitchen is totaly burned.')
  else:
    print('\nYou are late, you could escape but your home is totally burned')

#-Thirth scenario
elif option == 'call':
  print('\nYou realize that you have no choice but to call to superman, How are you going to do that? Using a super hero SIGNAL o SAYING his name laudly asking for rescue?')
  choice = input('\nEnter your choice (signal/saying): ')
  choice = choice.lower()
  if choice == 'signal':
    print('\nYou turn on the super hero signal but you see htat Batman has arrived, you used the wrong signal! Well you realize it worked in the same way because Batman used his technology to put of the fire.')
  elif choice == 'saying':
    print('\nYou go up to your roof and begin to call superman saying his name loud, in that moment Superman arrives quick and rescue your home with his super blast of air, congrantulations!')
  else:
    print('\nYou are late, you could escape but your home is totally burned')

#-Fourth scenario
elif option == 'pray':
  print('\nYou decide to pray because there is no time, so you can pray with your FAITH or using a magic AMULET.')
  choice = input('\nEnter your choice (FAITH/AMULET): ')
  choice = choice.lower()
  if choice == 'faith':
    print('\nWhen you begin to pray with faith a miracle happens, the rain began to fall, your home has been saved!')
  elif choice == 'amulet':
    print('\nYou pray with your magic amulet but you realize this does not work, run away from there!')
  else:
    print('\nYou are late, you could escape but your home is totally burned')

else:
  print('\nEy guys, select a valid option, I would like to play this game with you!')