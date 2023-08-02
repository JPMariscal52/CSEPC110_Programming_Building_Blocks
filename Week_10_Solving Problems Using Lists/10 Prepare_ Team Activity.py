#-10 Prepare: Team Activity
#-Multiple Lists

print('Enter the names and balances of bank accounts (type: quit when done)')

accounts = []
balances = []

account = ''

while account != 'Quit':

  account = input('\nWhat is the name of this account? ')
  account = account.title()

  if account != 'Quit':
    
    balance = float(input('What is the balance?'))
  
    accounts.append(account)
    print(accounts)
    balances.append(balance)
    print(balances)

total = 0

for money in balances:

  new_total = total + money
  total = new_total
  
print('\nAccount Information:')
print()

for i in range(len(accounts)):
    name_account = accounts[i]
    amount = balances[i]

    print(f"{i}. {name_account} - ${amount}")

average = total / len(balances)
print(f'\nTotal: ${total:.2f}')
print(f'Average: ${average:.2f}')

highest = 0
for i in balances:
  if i > highest:
    highest = i
  
print(f'Highest balance: ${highest}')

option = ''
while option != 'no':

  option = input('\nDo you want to update an account? ')

  if option != 'no':
    if option == 'yes':
      index = int(input('What account index do you want to update? '))
      new_amount = float(input('What is the new amount? '))

      balances[index] = new_amount
      print(balances)

      print('\nAccount Information:')
      print()

      for i in range(len(accounts)):
          name_account = accounts[i]
          amount = balances[i]
      
          print(f"{i}. {name_account} - ${amount}")

print('\nAccount Information:')
print()

for i in range(len(accounts)):
    name_account = accounts[i]
    amount = balances[i]

    print(f"{i}. {name_account} - ${amount}")

      



  

  
    


  

  