#!usr/bin/python

#File Name: python_12_6.py
#Developer: Martin Hernandez
#Date: 11/27/15
#E-mail: 7607920511m.h@gmail.com
#Description: Design a function that accepts an integer argument and returns the
#sum of all the integers from 1 and up to the number passed as an argument.
#For example, if 50 is passed as an argument, the function will return the sum
#of 1,2,3,4, . . . , 50.  Use recursion to calculate the sum.

def main():
    message(50,1)
    
def message(times,number):
    if times > 0:
        print(number)
        message(times - 1,number + 1)
  
main()
