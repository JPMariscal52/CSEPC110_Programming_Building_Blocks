#-03 Prepare: Preparation Material

#-Numeric data

#-When you use numeric data from a variable that you have created before to show it in a string you first have to convert the numeric data, because if you use it in the commun way, you will have an error when you run the code

#-Example
#age = 31
#print(age + 'is my age')

#-This is going to generate a Type error in our text compilator

#-To convert our numeric data we have to use the function str() inside the brackets

#age = 31
#print(str(age) + ' is my age')

#-Numbers stored as strings must be converted to numeric values before doing math

#Number1 = input('Enter number 1: ')
#Number2 = input('Enter number 2: ')

#-You have two options to convert them, to use function int() for integers numbers, or float() for decimal numbers

#print(int(Number1) + int(Number2))
#print(float(Number1) + float(Number2))

#-If you declare your operation in this way, the compilator will take the numeric data like a string and won't do the operation, only it will show you the numbers 

#print(Number1 + Number2)

#-Text variables
print('-Text variables-')

color = 'red'
animal = 'Dog' 

#-String with text variables
combined_words = color + ' ' + animal + "!"
print(combined_words)

print()

#-Numeric data
print('-Numeric inputs-')

boys = input()
girls = input()
print()

#-Numbers used like strings by default in input, the operation "add" doesn't happen 

print('-Numbers like strings-')
print(boys + girls)
print()

#-The operation only works using function "integer"
print('-Inputs using "int" function-')
print(int(boys) + int(girls))
print()

#-New variable created to displays add operation
print('-Inputs declared using a new variable-')
total_account = int(boys) + int(girls) 
print(total_account) 
print()

#-New variable displayed adding a string
print('-Result adding a string-')
print(str(total_account) + ' it is the total') 
print()

#-Casting the input in a Int variable
print('-Variable Int Double Input1-')
binteger = int(boys)
double_number = binteger * 2
print(double_number)
print()

#Variables used like numbers, the compilator will do the operation easily
print('-Variables as numbers-')
boys2 = 15
girls2 = 12
print(boys2 + girls2)
print()

#-You can create other variable to display the same operation
print('-Operation displayed like variable-')
total_account2 = boys2 + girls2 
print(total_account2)
print()

#-Casting numeric variables using "str" function 
print('-Numbers using Str function-')
bstring2 = str(boys2)
gstring2 = str(girls2)
print(bstring2 + gstring2)
print()

#-Here you can add your new string variable to other string
print('-String variable adding other string-')
print('These are' + ' ' + bstring2 + ' boys')
print()

#-Combining the input and int commands into one line
print('-Input and Int commands commbined-')
people_number = int(input("How many people are in the room? "))
print()

#-Add operation new variable 
print('-Input adding 8-')
print(people_number + 8)
print()

#-String adding numeric variable using Str function
print('-String adding Str in numeric variable-')
print('There are ' + str(people_number))