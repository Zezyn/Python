#!usr/bin/python

#File Name: project_8_10.py
#Developer: Martin Hernandez
#Date: 10/30/15
#E-mail: 7607920511m.h@gmail.com
#Description: Find and display the most frequent character in a string

import string

def main():
    sentence = userinput()
    characters = breakupstring(sentence)
    compare(characters, sentence)

def userinput(): #Gets a string from the user
    sentence = input("Please enter a sentence: ")
    sentence = sentence.lower()
    sentence = sentence.lstrip()
    sentence = sentence.replace(" ", "")
    return sentence.lower()

def compare(characters, sentence):
    compared = []
    charactertested = 0

    for characters in sentence:
        characteramount = characternumbers(characters, sentence)
        comparing = [characters], [characternumbers(characters, sentence)]
        if characteramount > charactertested:
            charactertested = characteramount
            display = characters, charactertested  
    print("The most repetitive character is \"", display[0], "\" repeating", display[1], "times.")

def characternumbers(characters, sentence):
    numbercount = 0

    for times in sentence:
        if times == characters:
            numbercount += 1
    return numbercount

def breakupstring(sentence):
    character = []

    for ch in sentence:
        character.append(ch)
    return character

main()
