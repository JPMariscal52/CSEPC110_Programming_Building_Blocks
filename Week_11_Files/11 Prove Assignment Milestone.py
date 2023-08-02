#-12 Prepare: Assignment Milestone

with open("life-expectancy.csv") as data_health:
  next(data_health)
  
  largest_expectancy = 0
  lowest_expectancy = 1000
  largest_expectancy2 = 0
  lowest_expectancy2 = 1000
  counter = 0
  total = 0
  
  year_of = int(input("Enter the year of interest: "))
  print()
  
  for data in data_health:
    
    data = data.strip()
    data_list = data.split(",")

    country = data_list[0]
    code = data_list[1]
    year = int(data_list[2])
    expectancy = float(data_list[3])

    if expectancy > largest_expectancy:
      largest_expectancy = expectancy
      la_country = country
      la_year = year
      
    if expectancy < lowest_expectancy:
      lowest_expectancy = expectancy
      lo_country = country
      lo_year = year

    if year <= year_of:

      counter += 1
      total += expectancy
      
      if expectancy > largest_expectancy2:
        largest_expectancy2 = expectancy
        la2_country = country
        la2_year = year
      

      if expectancy < lowest_expectancy2:
        lowest_expectancy2 = expectancy
        lo2_country = country
        lo2_year = year  
  
  print(f"The overall max life expectancy is: {largest_expectancy:.2f} from {la_country} in {la_year}")
  print(f"The overall min life expectancy is: {lowest_expectancy:.2f} from {lo_country} in {lo_year}\n")

  print(f"For the year: {year_of}\n")

  print(f"The average life expectancy across all countries was {total / counter:.2f}")
  print(f"The overall max life expectancy is: {largest_expectancy2:.2f} from {la2_country} in {la2_year}")
  print(f"The overall min life expectancy is: {lowest_expectancy2:.2f} from {lo2_country} in {lo2_year}")