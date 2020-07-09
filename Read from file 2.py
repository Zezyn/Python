#!usr/bin/python

#File Name: project_6_3_2.py
#Developer: Martin Hernandez
#Date: 10/07/15
#E-mail: 7607920511m.h@gmail.com
#Description: Reads the name and scores of a golfer (from file)

def main():
    golfer_file = open('golfers.txt', 'r')
    print('Golfer' + '\t\t' + 'Score')
    for line in golfer_file:
        print(line)
main()
