"""

File Name: project_2_1.py

Developer: Martin Hernandez

Date last modified: Fri September 11, 2015

Description: 
    (100 @ 0.21) Sales Prediction

A company has determined that its annual profit is typically 23 percent of total sales. Write a program that asks the user to enter the projected amount of total sales, and then displays the profit that will be made from that amount.

Hint: Use the value 0.23 to represent 23 percent.


The program should ask the user to enter a temperature in Celsius, and then display the temperature converted to Fahrenheit.

email address: 7607920511m.h@gmail.com@gmail.com

"""

#!/usr/bin/python

#Declare variables
perc = .23 #percentage to make annual profit

#Ask User for projected yearly sales
ysales = input("Please enter projected annual sales. ")
#Calculate .23 of total annual sales
profit = ysales * perc
#Display profit
print ("Here is the projected profit for the year. %s" + profit)

