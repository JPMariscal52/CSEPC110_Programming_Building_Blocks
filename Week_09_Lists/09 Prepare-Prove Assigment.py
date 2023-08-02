#-09 Prepare: Assignment Milestone
#-


print('Welcome to the Shopping Cart Program!')

items = []

option = 0

while option != 5:

  print('\nPlease select one of the following:')
  print('1. Add item')
  print('2. View cart')
  print('3. Remove item')
  print('4. Compute total')
  print('5. Quit')

  option = int(input('Please enter an action: '))

  if option != 5:

    if option == 1:

      item = input('What item would you like to add?')
      items.append(item)
      print(f"'{item.title()}' has been added to the cart.")
    

    elif option == 2:

      for product in items:

        print(product.title())


print('Thank you. Goodbye.')