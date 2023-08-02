#-05 Prepare: Preparation Material
#-Conditionals 
answer = input('Which of these sodas did you buy (Coca, Pepsi, Escuis? ')
if answer.lower() in('coca', 'pepsi', 'escuis') :
  price = float(input('How much did you pay? '))
  if price >= 1.00:
    tax = 0.07
    print(f'Tax rate is: {tax}')
  else :
    tax = 0 
    print(f'Tax rate is: {tax}')
else:
  print('That is great, drink water is better')