#-------------------------------------------------------------------------------
# Name: project_5_1.py          module2
#
# Purpose: Write a program that prompts the user to enter the account’s present
# value, monthly interest rate, and the number of months that the money will be
# left in the account. The program should pass these values to a function that
# returns the future value of the account, after the specified number of months.
# The program should display the account’s future value.
#
# Author:      Martin Hernandez
#
# Created:     10/02/15
#
# Copyright:   (c) Student 2015
#-------------------------------------------------------------------------------

import math

def main():
    #Gets the users information.
    money, interest, time = userinput()

    print(" $%.2f " % Interest(money, interest, time))

#Create a funtion to prompt user for input ($ in account, interest rate, months
#to calculate.
def userinput():
    money = float(input('How much money is in the account? '))
    interest = float(input('What is the interest rate?'))
    time = int(input('How many months will you leave the money in the account?'))
    return money, interest, time

#Create a function to calculate interest rate
#F = P X ( 1 + i)t
def Interest(money, interest, time):
    future_value = money*((1+interest)**time)
    return future_value

main()