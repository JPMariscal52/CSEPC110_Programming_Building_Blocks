#-10 Prepare: Team Activity
#-Multiple Lists

print('Please enter the items of the shopping list (type: quit to finish):')

products = []
product = ''

while product != 'Quit':

  product = input('Item: ')
  product = product.title()
 
  
  if product != 'Quit':
    products.append(product)
    print(products)

print('\nThe shopping list is:')
for item in products:
  print(item)

print('\nThe shopping list with indexes is:')
for i in range(len(products)):
    item = products[i]
    print(f"{i}. {item}")

new_item = ''

while new_item != 'Quit':

  index = int(input('\nWhich item would you like to change?'))
  new_item = input('What is the new item?')
  new_item = new_item.title()

  if new_item != 'Quit':
    products[index] = new_item
    print(products)
    
print("\nThe shopping list with indexes is:")

for i in range(len(products)):
    item = products[i]
    print(f"{i}. {item}") 

  
    


  

  