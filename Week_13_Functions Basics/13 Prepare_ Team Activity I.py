#-13 Prepare: Team Activity I
#-Areas of Shapes Revisited

shape = ''

def compute_area_square(side):
  square_area = side ** 2
  return square_area

def compute_area_rectangle(side1, side2):
  rectangle_area = side1 * side2
  return rectangle_area

def compute_area_circle(ratio):
  circle_area = 3.14 * (ratio ** 2)
  return circle_area

size1 = int(input('Enter the value for side1: '))
size2 = int(input('Enter the value for side2: '))
ratio = int(input('Enter the value for ratio: '))

area = compute_area_square(size1)
area2 = compute_area_rectangle(size1, size2)
area3 = compute_area_circle(ratio)

while shape != 'quit':

  print("Square-1, Rectangle-2, Circle-3")
  print("When you want to finish write 'quit'")
  shape = input("Which shape do you want to display? ")

  if shape == '1':
    print(area)
  
  elif shape == '2':
    print(area2)
  
  elif shape == '3':
    print(area3)

  else:
    print('Try again')

print('Good bye')


    

    


