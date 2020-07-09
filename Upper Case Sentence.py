#!usr/bin/python

#File Name: project_8_10.py
#Developer: Martin Hernandez
#Date: 11/02/15
#E-mail: 7607920511m.h@gmail.com

#Description: Word Seperator -- Exercise 11
#Write a program that accepts as input a sentence in which all of the words are run together but the
#first character of each word is uppercase. Convert the sentence to a string in which the words are
#seperated by spaces and only the first word starts with an uppercase letter. for example the string
#“StopAndSmellTheRoses.” would be converted to “Stop and smell the roses.”


import string

def main():
    sentence = userinput()
    print(checkch(sentence))
    
def userinput():
    sentence = input("Please enter a sentence that runs together with the first letter of each word as a capitol: ")
    return sentence

def checkch(sentence):
    chprint = ""
    for ch in sentence:
        if ch.isupper():
            chprint += " " + ch
        else:
            chprint = chprint + ch
    return chprint

main()
