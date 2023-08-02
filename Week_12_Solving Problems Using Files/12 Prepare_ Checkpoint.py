#-12 Prepare: Checkpoint

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest_age = 100
youngest_name = ""

for data in people:
  
  data = data.strip()
  data = data.split()
  print(data)
  
  name = data[0]
  age = int(data[1])

  if age < youngest_age:
    youngest_age = age
    youngest_name = name

print(f"{youngest_name} is {youngest_age} and this makes him the youngest guy here")
    

    

  














    
    


