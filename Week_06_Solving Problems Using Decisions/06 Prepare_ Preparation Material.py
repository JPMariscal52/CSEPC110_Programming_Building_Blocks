#-06 Prepare: Preparation Material
#-Remember, the function "if" only works if the condition gets a true value.
is_hot = True

# You can check the value of the variable directly
if is_hot:
    print("It's hot")

# It works, but is redundant (and therefore bad practice) to check if it is True:
if is_hot == True:
    print("It's hot")

is_hot = False

# Using the "not" keyword
if not is_hot:
    print("It is not hot")

# It works, but is generally avoided to check if it is false:
if is_hot == False:
    print("It is not hot")

is_hot1 = True
is_hot2 = True

# You can check the value of the variable directly
if is_hot1:
    print("It's hot1")

# It works, but is redundant (and therefore bad practice) to check if it is True:
if is_hot2 == True:
    print("It's hot2")

