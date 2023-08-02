#-05 Teach: Team Activity
#-Grade Calculator 
'''
grade = float(input('What is your grade percentage? '))

if grade >= 90 :
  print('Your letter grade is: A')
  print('You have done it exellent!')

elif grade >= 80 :
  print('Your letter grade is: B')
  print('You have done it well!')

elif grade >= 70 :
  print('Your letter grade is: C')
  print('It is enough, but you can improve the next')

elif grade >= 60 :
  print('Your letter grade is: D')
  print('You have not gotten it!')

elif grade < 60 :
  print('Your letter grade is: F')
  print('You have not gotten it!')

if grade >= 70:
    print("Congratulations! You have passed the class!")
else:
    print("You can get it next time!")
'''

grade = int(input("What is your grade percent? "))
s = grade % 10

if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

if grade < 93 and grade > 59 :
  if s >= 7:
    sign = '+'
  elif s > 2 and s < 7:
    sign = ' '
  elif s < 3:
    sign = '-'
else:
  sign = ' '
    

print(f"Your letter grade is: {letter}{sign}")

if grade >= 70:
    print("Congratulations! You have passed the class!")
else:
    print("You can get it next time!")
  