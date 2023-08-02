#- 02 Prove: Assignment - Word Games (Mad Lib)

print('Welcome to this Mad Lib')
print('To start, please enter the following:')
print()
adjective = input('Adjective: ')
animal = input('Animal: ')
verb1 = input('Verb: ')
exclamation = input('Exclamation: ')
verb2 = input('Verb: ')
verb3 = input('Verb: ')

print()

print('This is the story you have created, have fun!')

print()

print('The other day, I was really in trouble. It all started when I saw a very')
print(adjective.lower() + ' ' + animal.lower() + ' ' + verb1.lower() + ' ' + 'down the hallway. "' + exclamation.capitalize() + '!" I yelled. But all')
print('I could think to do was to ' + verb2.lower() + ' over and over. Miraculously,')
print('that caused it to stop, but not before it tried to' + ' ' + verb3.lower())
print('right in front of my family.')

print()

#-This is the part I have added to my code, it beggins with these two questions, then you can enter your name 
#-to be part of the game.

print('Do you like the story?')

print('Would you like to be part of the story?')

print()

#-Here you can enter your name 

name = input('If you would like to be part of it, please enter your name: ')

print()

#- I have modified the text of the story in third person

print('The other day,' + ' ' + name.capitalize() + ' ' + 'was really in trouble. It all started when' + ' ' + name.capitalize() + ' ' + 'saw a very')
print(adjective.lower() + ' ' + animal.lower() + ' ' + verb1.lower() + ' ' + 'down the hallway. "' + exclamation.capitalize() + '!" ' + ' ' + name.capitalize() + ' yelled. But all')
print(name.capitalize() + ' could think to do was to ' + verb2.lower() + ' over and over. Miraculously,')
print('that caused it to stop, but not before it tried to' + ' ' + verb3.lower())
print('right in front of a family.')