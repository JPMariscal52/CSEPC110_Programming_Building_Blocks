#-04 Prepare: Checkpoint - Unit Conversion
#-Make a dregree calculator to convert Fahrenheit to Celcius
fahrenheit_degrees = float(input('What is the temperature in Fahrenheit? '))
celcius_degrees = (fahrenheit_degrees - 32) * (5 / 9)
print(f'The temperature in Celsius is {celcius_degrees:.1f} degrees.')