#-09 Prepare: Preparation Material

clients = []

clients.append('Emily')
clients.append('Emily')
clients.append('Emily')

print(clients)

print()

clients2 = []
new_client = ''

while new_client != 'quit':
  new_client = input('What is the name of a client?')
  clients2.append(new_client)

print()

for client in clients2:
  print(client)


tips = [12.25, 13.95, 8.5]

running_total = 0

for tip_amount in tips:
  running_total += tip_amount


print(f"The total is: {running_total:.2f}")