#-10 Prepare: Assignment Milestone
#-Shopping Cart Program
print('*' * 37)
print('Welcome to the Shopping Cart Program!')
print('*' * 37)
items = ['']
prices = [0]
discount = [0]

option = 0

while option != 6:

  print('\nPlease select one of the following:\n')
  print('-' * 18)
  print('1. Add item')
  print('2. View cart')
  print('3. Remove item')
  print('4. Compute total')
  print('5. Get discount')
  print('6. Quit')
  print('-' * 18)

  option = int(input('\nPlease enter an action: '))

  if option != 6:

    if option == 1:

      item = input('What item would you like to add? ')
      items.append(item)
      price = float(input(f"What is the price of '{item.title()}'? "))
      prices.append(price)
      print('*' * 34)
      print(f"'{item.title()}' has been added to the cart.")
      print('*' * 34)

    elif option == 2:
        print()

        for i in range(1,len(items)):
        
          item = items[i]
          price = prices[i]

          print(f"{i}. {item.title()} - ${price}")

    elif option == 3:

      index = int(input('Which item would you like to remove? '))
      items.pop(index)
      prices.pop(index)

      print('Item removed.')

    elif option == 4:

      total = 0
      print()

      for money in prices:
  
         new_total = total + money
         total = new_total
  
      print(f"The total price of the items in the shopping cart is ${total:.2f}")

      if discount[0] > 0:
        total_discount = total - (discount[0] * total)
        print(f'The total with your discount is: ${total_discount:.2f}')

    elif option == 5:

      print('\nEnter the code "PC101" to get a 10% discount')
      print('Enter the code "PC102" to get a 15% discount')
      print('Enter the code "PC103" to get a 20% discount')
      code = input('\nEnter your code: ')
      code = code.lower()

      if code == 'pc101':
        discount.pop(0)
        discount.append(0.1)
        print('Well done, now you have your 10% discount!')

      elif code == 'pc102':
        discount.pop(0)
        discount.append(0.15)
        print('Well done, now you have your 15% discount!')

      elif code == 'pc103':
        discount.pop(0)
        discount.append(0.20)
        print('Well done, now you have your 20$ discount!')

      else:
        print('Enter a valid code')   

    
   

print('Thank you. Goodbye.')