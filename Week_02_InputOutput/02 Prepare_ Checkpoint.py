#-02 Prepare: Checkpoint - Formatting Strings
#-We'll use the James Bond format phrase for this exercise

first_name = input('Please, enter your first name: ')
last_name = input('Please, enter your last name: ')

print()


#-First way to declare variables, using sign +
#print('Your name is ' + last_name.title() + ', ' + first_name.title() + ' '+ last_name.title() + '.')

#-Second way to declare variables, using place holders
print('Your name is {1}, {0} {1}.'.format(first_name.title(), last_name.title()))

#-Third way to declare variables, using function 'f'
#print(f'Your name is {last_name.title()}, {first_name.title()} {last_name.title()}.')
