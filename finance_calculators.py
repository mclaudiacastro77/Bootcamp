# The program allows the user to access two different financial calculators: 
# an investment calculator and a home loan repayment calculator.

import math

first_output = '''
Investment - to calculate the amount of interest you'll earn on your investment.
Bond - to calculate the amount you'll have to pay on a home loan.
'''
print(first_output)

option_selection_1 = "investment"
option_selection_2 = "bond"

option_selection = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
option_selection = option_selection.lower()

if option_selection != option_selection_1 and option_selection != option_selection_2:
    print("Type a valid option.") 

print("")
# Investment calculator
if option_selection == "investment":
    # Money amount 
    P = float(input("Enter the amount of money that you are depositing: "))
    # Interest rate 
    r = float(input("The interest rate (e.g.8): ")) 
    r = r/100                         
    # Years 
    t = int(input("The number of years you plan on investing: "))
    interest = input("Do you want simple or compound interest? (Simple/Compound) ")
    interest = interest.lower()

    # Simple interest
    if interest == "simple":
        A = P * (1 + r * t) 
        A = round(A,2)  
        print("")
        print(f"Future investment value: {A}")
    
    # Compound interest
    elif interest == "compound":
        A = P * math.pow((1 + r), t)
        A = round(A,2)  
        print("")
        print(f"Future investment value: {A}")  

# Home loan repayment calculator
elif option_selection == "bond":
    # House value
    P = int(input("The present value of the house (e.g.100000): "))
    # Monthly interest rate
    i = float(input("The interest rate (e.g.7): "))
    i = (i/100)/12
    # Number of months to repay the bond
    n = int(input("The number of months you plan to take to repay the bond. (e.g.120): "))
    repayment = (i * P)/(1 - (1 + i)**(-n))
    repayment = round(repayment,2)
    print("")
    print(f"You will repay each month: {repayment}")



    
  



