#!usr/bin/python

#File Name: project_6_3.py
#Developer: Martin Hernandez
#Date: 10/07/15
#E-mail: 7607920511m.h@gmail.com
#Description: Write a program that reads and writes a series of golf scores to a file.

def main():
    newgolfer = 'y'
    while (newgolfer == 'y') or (newgolfer == 'Y'):
        golfer = input('Enter the name of a golfer: ')
        golfer_score = input('Enter the golfer\'s score: ')
        print('Golfer:', golfer, " ", 'Golfer\'s Score:', golfer_score)
        golfer_file = open('golfers.txt', 'a')
        golfer_file.write((golfer) + '\t\t' + (golfer_score) + '\n')
        golfer_file.close()
        newgolfer = input("Would you like to add another golfer? ")
main()
