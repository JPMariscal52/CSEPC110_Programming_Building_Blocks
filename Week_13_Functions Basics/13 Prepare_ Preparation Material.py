#-13 Prepare: Preparation Material

def regards_corning():
    print("Hello world from Corning")

regards_corning()
print()
regards_corning()


def double_value(value):
  doble = value * 2
  return doble

number = int(input("Enter a value: "))
number2 = int(input("Enter a value: "))
x = double_value(number)
double_value(number2)

print(x)

def print_message(the_message):
    print(the_message)

# it works just fine to use the same variable name as the function did...
the_message = "Message 1"
print_message(the_message)

# but it also works to use a different variable...
user_message = "Message 2"
print_message(user_message)

print_message(x)
