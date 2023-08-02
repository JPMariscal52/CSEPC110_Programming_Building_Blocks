#-13 Prove: Assignment
#-Wind Chill Calculations

def f_to_celsius(T):
  return 9/5 * T + 32

def wind_chill_formula(V,T):
    return 35.74 + (0.6215*T) - (35.75*(V**0.16)) + (0.4275*T*(V**0.16))


T = float(input("What is the temperature? "))
celsius = f_to_celsius(T)
D = input("Fahrenheit or Celsius (F/C)? ")
D = D.lower()


for v in range(5,65,5):
  
  if D == 'f':
    wind_chill = wind_chill_formula(v,T)
  elif D == 'c':
    T= celsius
    wind_chill = wind_chill_formula(v,celsius)
    
  
  print(f"At temperature {T:.2f}F, and wind speed {v} mph, the windchill is: {wind_chill:.2f}F")