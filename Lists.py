#!usr/bin/python

#File Name: project_7_1.py
#Developer: Martin Hernandez
#Date: 10/16/15
#E-mail: 7607920511m.h@gmail.com
#Description: Design a program that asked the user to enter a series of 20 numbers.
#           The program should store the numbers in a list and then display the following data:
#           lowest number, highest number, total numbers in list, average number.

def main():
    print("Please enter 20 numbers: ")
    numberlist = []
    getinput(numberlist)
    lowestnumber(numberlist)
    highestnumber(numberlist)
    totalnumbers(numberlist)
    averagenumber(numberlist)
    
#Create a function to get 20 numbers from user
def getinput(numberslist):
    for i in range(5):
        numberslist.append(int(input("Number" + str(i+1) + ":  ")))

#Function for lowest number        
def lowestnumber(numberlist):
    print("The lowest number is:", min(numberlist))

#Function for highest number    
def highestnumber(numberlist):
    print("The highest number is:", max(numberlist))

#Function for total amount of numbers
def totalnumbers(numberlist):
    print("Total amount of numbers:", len(numberlist))

#Function for average of numbers in the list
def averagenumber(numberlist):
    print("The average of the list of numbers is:", sum(numberlist)/(len(numberlist)))
    
main()

