#-04 Prove: Milestone - Meal Price Calculator

child_meal = float(input("\nWhat is the price of a child's meal? "))
adult_meal = float(input("What is the price of a adult's meal? "))
children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))

#-I added this additional question where you can ask for a dessert, being specific an ice cream.
print('You can add Ice Cream for $0.50 ea')
dessert = float(input('How many ice creams do you want? '))

tax_rate = float(input("What is the sales tax rate? "))

#-In this question you can decide if you make a donation or not, if you do, only put the amount of your donation, if you don't, only put zero.
print('Would you like to support education making a donation to BYU-Pahtway Worldwide?')
donation = float(input("How much would you like to donate (If you don't put 0)? "))

#-This string '-' replaces blank space
print('-' * 75)

subtotal = (child_meal * children) + (adult_meal * adults) + (dessert * 0.5)
print(f'Subtotal: ${subtotal:.2f}')
sales_tax = subtotal * (tax_rate / 100)
print(f'Sales Tax: ${sales_tax:.2f}')

#-I have added the donation here because donations are tax exempt 
total = subtotal + sales_tax + donation
print(f'Total: ${total:.2f}')

#-This string '-' replaces blank space
print('-' * 75)

payment = int(input('What is your payment amount? '))

change = payment - total
print(f'Change: ${change:.2f}')