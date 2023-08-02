#-12 Prepare: Preparation Material

with open("data.txt") as datwer:
  
  next(datwer)

  max = 0
  max_course = ""
  min = 1000
  min_course = ""
  for course in datwer:
    
    course = course.strip()
    data_course = course.split()
    
    name_course = data_course[0]
    number = int(data_course[1])
    
    print(number)
    
    if number > max:
      max = number
      max_course = name_course

    if number < min:
      min = number
      min_course = name_course
  
  print(f"The highest number is: {max}")
  print(f"The product with the maximum price is: {max_course}")
  print(f"The lowest number is: {min}")
  print(f"The product with the maximum price is: {min_course}")


    
    


