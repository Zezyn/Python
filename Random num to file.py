#!usr/bin/python

#File Name: project_6_1.py
#Developer: Martin Hernandez
#Date: 10/07/15
#E-mail: 7607920511m.h@gmail.com
#Description: Write a program that writes a series of random numbers to a file. Each random number should be in the range of one through five hundred. The application should let the user specified how many random numbers the file will hold.
import random

def main():
    
    numberoftimes = int(input('How many numbers random numbers would you like to put in the file?'))

    for i in range(numberoftimes):
        number = random.randint(1, 500)
        print('A number is:', number)
        number_file = open('project_6.txt', 'a')
        number_file.write(str(number) + '\n')
        number_file.close()
main()
