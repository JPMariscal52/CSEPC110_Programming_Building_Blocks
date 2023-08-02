#-06 Prepare:Checkpoint
#-Qualifying for a Loan

print('Welcome to your loan qualifier')

loan_s = int(input('\nHow large is the loan? '))
credit_h = int(input('How good is your credit history? '))
income_h = int(input('How high is your income? '))
payment_d = int(input('How large is your down payment? '))

if (credit_h >= 7 and income_h >= 7) or ((credit_h >= 7 or income_h >= 7) and payment_d >= 5) or (credit_h == 4 and (income_h >= 7 or payment_d >= 7)) or (credit_h == 4 and (income_h >= 4 and payment_d >= 4)):
  is_qualified = True

else:
  is_qualified = False

if is_qualified:
    print("\nYou qualify for a loan, congratulations!.")
else:
    print("\nYou don't qualify for a loan.")




#-Sample solution by instructor

"""
File: check06_sample.py
Author: Brother Burton

Purpose: Practice if statements with loan questions
"""
'''
print("For each of these questions, please provide a 1-10 rating:")

loan_size = int(input("How large is the loan? "))
credit = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
down_payment = int(input("How large is your down payment? "))

# For safety sake, I always like to set the variable to a default value of False
# That way, if for some reason it doesn't get set it in our rules below it will
# not be left "undefined" and cause an error, and I don't like to set the default
# to be True, because I don't want to accidentally give someone a loan!
should_loan = False

if loan_size >= 5:
    if credit >= 7 and income >= 7:
        should_loan = True
    elif credit >= 7 or income >= 7:
        if down_payment >= 5:
            should_loan = True
        else:
            should_loan = False
    else:
        should_loan = False
else: # This means its a small loan
    if credit < 4:
        should_loan = False
    else:
        if income >= 7 or down_payment >= 7:
            should_loan = True
        elif income >= 4 and down_payment >= 4:
            should_loan = True
        else:
            should_loan = False

if should_loan:
    print("The decision is yes. This is a good loan.")
else:
    print("The decision is no. You should not loan this money.")

# In case you are wondering, all of the above if/elif/else statements
# could be combined into one great big huge if statement, but I've left it
# this way to better match the rules that were provided.
'''