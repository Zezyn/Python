#!usr/bin/python

#File Name: project_4_1.py
#Developer: Martin Hernandez
#Date: 9/22/15
#E-mail: 7607920511m.h@gmail.com
#Description: Write a program that calculates the amount of money a person would earn over 
#a period of time if his or her salary is one penny the first day two pennies the second day
#and continues to double each day. The program should ask the user for the number of days. 
#Display a table showing what the salary was for each day and then show the total pay at 
#the end of the period. The output should be displayed in a dollar amount, not the number 
#of pennies.

#Declare Variables
pennies = 0.01

#Ask user for the amount of days to calculate.
days = input('How many days would you like to calculate?\n')
days = int(days) + 1

print('\n', '\t', 'Days', '\t' 'Salary')
print('\t---------------')
#Calculate days and coin
for countingdays in range(1, days):
    print('\t', countingdays, '\t$', pennies, sep='')
    pennies = pennies * 2
