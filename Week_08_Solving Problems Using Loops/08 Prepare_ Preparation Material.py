#-08 Prepare: Preparation Material
#-For Loops

#-First section
print('---First example using an array---\n')
items = ["crayon", "scissors", "paper", "glitter glue", "markers", "pens", "crayon", "scissors", "paper", "glitter glue", "markers", "pens"]

for item in items:
    print(f"The item is: {item}")
  
#-Here I have added an if which is activated when 'item' equals to 'pens'
if item == "pens":
  print('well done')


#-Second section
print('\n---Second example using a range---')
#-This time you can loop using a range, only thing you need to do it is specifying the range
for number in range(10):
    print(number)

#-Third section
#- I'm using nested for loops, remember you can use the letters i,j,k to name the numeric variables
print('\n---Third example Loops within loops---')
for i in range(5):
    print(i)
    for j in range(10, 13):
        print(f"--{j}")
        if j == 12:
          print('Good lock')

#-Fourth section
#-You can loop through a string, in this case only one word
print('\n---Fourth example looping throug a string---')
first_name = 'Brigham'
for letter in first_name:
    print(f"The letter is: {letter}")

#-Fifth section
#-The postion of the letter you are specifying
print('\n---Fifth example position and index---')
first_name = "Brigham"

fourth_letter = first_name[3]
print(fourth_letter)

#-Sixth section
print('\n---Sixth example specifying---')
first_name = "Brigham"

#-Notice by using enumerate, we specify both i and letter
for i, letter in enumerate(first_name):
    print(f"The letter {letter} is at position {i}")