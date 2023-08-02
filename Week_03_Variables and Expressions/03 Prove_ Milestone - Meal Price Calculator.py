#- 03 Prove: Milestone - Meal Price Calculator

child_meal = float(input("\nWhat is the price of a child's meal? "))
adult_meal = float(input("What is the price of a adult's meal? "))
children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))

#-I added this question where you could ask for a specific dessert, an ice cream.

print('You can add Ice Cream for $0.50 ea')
dessert = float(input('How many ice creams do you want? '))
tax_rate = float(input("What is the sales tax rate? "))

subtotal = (child_meal * children) + (adult_meal * adults) + (dessert * 0.5)
print(f'\nSubtotal: ${subtotal}')