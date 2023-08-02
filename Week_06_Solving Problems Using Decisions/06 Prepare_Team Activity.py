#-06 Prepare:Team Activity
#-Amusement Park Rides

print('Welcome to this Amusement Park Rides')

age_1 = int(input ('\nWhat is the age of the first rider? '))
height_1 = int(input ('What is the height of the first rider? '))
rider = input ('Is there a second rider (yes/no)? ')
rider = rider.lower()

if age_1 >= 12 and age_1 < 18:
  passport = input('Does the first rider has a golden passport (yes/no)? ')
  passport = passport.lower()

  if rider == 'yes':
    age_2 = int(input ('What is the age of the second rider? '))
    height_2 = int(input ('What is the height of the second rider? '))
    if age_2 >= 12 and age_2 < 18:
      passport2 = input('Does the second rider has a golden passport (yes/no)? ')
      passport2 = passport2.lower()
    
  
      if height_1 < 36 or height_2 < 36:
        can_ride = False
      else:
        if (age_1 >= 18 or passport == 'yes')  or (age_2 >= 18 or passport2 == 'yes'):
          can_ride = True
        elif (age_1 >= 16 and age_2 >= 14) or (age_1 >= 14 and age_2 >= 16):
          can_ride = True
        elif age_1 >= 12 and age_1 < 18 and age_2 >= 12 and age_2 < 18:
          if height_1 >= 52 and height_2 >= 52:
            can_ride = True
        else:
          can_ride = False
  else:
    if (age_1 >= 18 or passport == 'yes') and height_1 >= 62:
      can_ride = True 
    else:
      can_ride = False
  
  if can_ride:
    print('\nWelcome to the ride. Please be safe and have fun!')
  else:
    print('\nSorry, you may not ride.')
  