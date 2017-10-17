#!usr/bin/python

#File Name: project_6_2.py
#Developer: Martin Hernandez
#Date: 10/07/15
#E-mail: 7607920511m.h@gmail.com
#Description: Read and print information from file

def main():
    number_file = open(r'c:\College\Python\project_6.txt', 'r')
    print('Information from file:')
    for line in number_file:
        print(line)
main()
