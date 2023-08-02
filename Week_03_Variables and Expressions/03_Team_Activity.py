#-03 Teach: Team Activity
#-AREAS OF A SHAPES

import math 
#-Area of the square
l_square = float(input('What is the length of a side of the square? '))
a_square = l_square ** 2
print('The area of the square is: ' + str(a_square))

#-Area of the rectangule
l_rectangule = float(input('What is the length of rectangule? '))
w_rectangule = float(input('What is the width of the rectangule? '))
a_rectangule = l_rectangule * w_rectangule
print('The area of the rectangule is: ' + str(a_rectangule))

#-Area of the circle
r_circle = float(input('What is the radius of the circle? '))
a_circle = 3.14 * (r_circle**2)
print('The area of the circle is: ' + str(a_circle))
print()

#-Square, circle, cube, and sphere
s_value = float(input('What is the single length value? '))
square = s_value ** 2
circle = 3.14 * (s_value ** 2)
cube = s_value ** 3
sphere = (4/3) * 3.14 * (s_value ** 3)
print('The area of the square is: ' + str(square))
print('The area of the circle is: ' + str(circle))
print('The volume of the cube is: ' + str(cube))
print('The volume of the sphere is: ' + str(sphere))

math.pi 
print(math.pi)