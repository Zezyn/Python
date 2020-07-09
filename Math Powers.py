#!usr/bin/python

#File Name: python_12_7.py
#Developer: Martin Hernandez
#Date: 11/28/15
#E-mail: 7607920511m.h@gmail.com
#Description: Design a function that uses recursion to raise a number to a power
#The function should accept two arguments: the number to be raised and the
#exponent. Assume that the exponent is a nonnegative integer.

def main():
    #number = input('What is the positive number you want to raise to a power? ')
    #power = input('What is the positive exponent? ')
	
    number = 2
    power = 2
    total = 0
    
    powers(number, power, total)
    
def powers(number, power, total):
    if power < 0:
        total = number * total
        print(total)
        powers(number, power - 1, total)
             
main()
