#-02 Teach: Programming Activity - Id Badge Generator
print('Please, enter the following information: \n')

first_name = input('First name: ')
last_name = input('Last name: ')
Email = input('Email Address: ')
PhoneN = input('Phone number: ')
Job = input('Job title: ')
ID = input('ID Number: ')

#-Additional information

Hair_color = input('Hair color: ')
Eye_color = input('Eye color: ')
Month = input('Starting month: ')
Training = input('Completed additional training? ')

#-This function print with only one space it is to separate ID card when you finish typing data
print()

#-Second way to declare variables, using place holders

print('--------------------------')
print('{1}, {0}'.format(first_name.title(), last_name.upper()))
print(Job.title())
print(ID)
print()
print(Email.lower())
print(PhoneN)
print()
print('Hair: ' + Hair_color.capitalize() + '            ' + 'Eyes: ' + Eye_color.capitalize())
print('Month: ' + Month.capitalize() + '         ' + 'Training: ' + Training.capitalize())
print('--------------------------')


#-This program was written by instructor as example if you weren't able to finish this exercise

#print("Please enter the following information:")

#print()

#-Ask for the basic information
#first = input("First name: ")
#last = input("Last name: ")
#email = input("Email address: ")
#phone = input("Phone number: ")
#job_title = input("Job title: ")
#id_number = input("ID Number: ")

#-Ask for the additional information
#hair_color = input("Hair color: ")
#eye_color = input("Eye color: ")
#month = input("Starting Month: ")
#training = input("Completed additional training? ")

#-Now print out the ID Card
#print("\nThe ID Card is:")
#print("----------------------------------------")
#print(f"{last.upper()}, {first.capitalize()}")
#print(job_title.title())
#print(f"ID: {id_number}")
#print()
#print(email.lower())
#print(phone)
#print()

#-There are various ways to accomplish the spacing

#-In this approach, I told it that hair_color will take exactly 15
#-spaces, and month will take 14. That way, the next columns will
#-line up. I had to do month 14 (instead of 15) because the word
#-'Month' that came before my value was one letter longer.

#print(f"Hair: {hair_color:15} Eyes: {eye_color}")
#print(f"Month: {month:14} Training: {training}")
#print("----------------------------------------")