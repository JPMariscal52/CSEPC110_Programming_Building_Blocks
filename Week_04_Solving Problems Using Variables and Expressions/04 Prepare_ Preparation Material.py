#-04 Prepare: Preparation Material
#-Format strings - Rounding numbers

#-Using format (:.#f) to define number of decimals
tacos = 3
people = 8
tacos_per_people = tacos / people

#-Round to 1 decimal
print(f"There are {tacos_per_people:.1f} per each one")

#-Round to 2 decimal
print(f"There are {tacos_per_people:.2f} per each one")

#-Round to 3 decimal
print(f"There are {tacos_per_people:.3f} per each one")

#-Using (:.#e) scientific notation
#-Scientific notation with 3 digits of precision
distance = 1000000000
print(f"This is the distance {distance:.3e} meters")

#-Scientific notation with 5 digits of precision
distance = 10 * 10 * 150
print(f"This is the distance {distance:.5e} meters")

#-Thousands grouping (:,) (:_)
number = 4444555895 / 3
print(f"The number is {number:,}")
#-Combining with rounding decimals
print(f"The number is {number:,.2f}")

print(f"The number is {number:_}")
#-Combining with rounding decimals
print(f"The number is {number:,.2f}")

#-Using math-library functions
import math

radius = 5
area = math.pi * (radius ** 2)
print(f"The area is: {area:.3f}")

weight = 5.65

lower = math.floor(weight)
print(lower)
# Output: 5

higher = math.ceil(weight)
print(higher)
# Output: 6