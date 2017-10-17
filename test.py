income = input("Enter your income please:")

tax = 0.00
if income > 50000 and income <= 75000:
    tax = .01
elif income > 75000 and income <= 100000:
    tax = .02
elif income > 100000 and income <= 250000:
    tax = .03
elif income > 250000 and income <= 500000:
    tax = .04
else:
    tax = .05

taxes_owed = (income * tax)
    
print('Taxes due are: ')
print(taxes_owed)