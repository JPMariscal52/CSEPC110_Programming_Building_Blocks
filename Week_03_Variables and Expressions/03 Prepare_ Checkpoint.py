#-03 Prepare: Checkpoint
#-NUMERIC DATA TYPES

#-Age Question
print()
actual_age = int(input('How old are you? '))
next_age = actual_age + 1
print('On your next birthday, you will be ' + str(next_age))
print()

#-Eggs Question
num_eggs = input('How many eggs cartons do you have? ')
eggs_cartons = int(num_eggs) * 12
print('You have ' + str(eggs_cartons) + ' eggs')
print()

#-Cookies Question
cookies_num = input('How many cookies do you have? ')
numcookies = int(cookies_num)
people_num = input('How many people are there? ')
numpeople = int(people_num)
assigned_cookies = numcookies / numpeople
print('Each person may have ' + str(float(assigned_cookies)) + ' cookies')