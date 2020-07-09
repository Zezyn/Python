#!usr/bin/python

#File Name: project_5_2.py
#Developer: Martin Hernandez
#Date: 10/3/15
#E-mail: 7607920511m.h@gmail.com
#Description: Write a program that lets
#the user play the game of rock, paper, scissors against the computer.

#import funtions here
import random

#Declare Variables
rock = 1
paper = 2
scissors = 3

def main():
    autonumber = random.randint(1, 3)
    print(autonumber)
    user = user_input()
    winner = calculate_winner(computer, user)
    print(winner)
    choice = again()

#check to see if user would like to play again
    if choice == y:
        main()
    else:
        print('\nThank you for playing\n')

#Ask user for his choice, (Rock paper scissors)
    def users_input():
        print('\nWelcome to Paper, Rock Scissors! \n')
        print('Please select an option: \n')
        print('1) Paper \n')
        print('2) Rock \n')
        print('3) Scissors \n')
        a_choice = input('1, 2 or 3? \n')
        return a_choice

#Calculate winner and display
    def calculate_winner(computer, user):
        if computer == rock:
            if user == rock:
                winner = ('\nComputer chooses Rock.\n It\'s a tie\n')
            elif user == paper:
                winner = ('\nComputer chooses Rock.\n Paper covers Rock.\n You Win!\n')
            else: user == scissors
            winner = ('\nComputer chooses Rock.\n Rock smashes Scissors.\n Computer Wins!\n')
        elif computer == paper:
            if user == paper:
                winner = ('\nComputer chooses Paper.\n It\'s a tie.\n')
            elif user == rock:
                winner = ('\nComputer chooses Paper.\n Paper covers Rock.\n Computer wins!\n')
            elif user == scissors:
                winner = ('\nComputer chooses Paper.\n Scissors cuts Paper.\n You Win!\n')
        else:
            computer == scissors
            if user == scissors:
                winner = ('\nComputer chooses Scissors.\n It\'s a tie.\n')
            elif user == rock:
                winner = ('\nComputer chooses Scissors.\n Rock crushes Scissors.\n You Win!\n')
            elif user == paper:
                winner = ('\nComputer chooses Scissors.\n Scissors cuts Paper. \n Computer Wins!\n') 
    return winner
#Ask user to play again
    def again():
        choice = input('\nWould you to play again? (y or n)\n')
    return choice

main()
