#!usr/bin/python

#File Name: project_7_2.py
#Developer: Martin Hernandez
#Date: 10/17/15
#E-mail: 7607920511m.h@gmail.com
#Description: Write a program that calculates the total number of correct and
#incorrect answers from a DMV test. Display pass or fail and incorrect question
#numbers

def main():
    answers = readanswers()
    test = readtest()
    correct, incorrect = comparetests(test, answers)
    grade(correct, incorrect)
    
#Read answers.txt file which stores the test answers 
def readanswers():
    testanswers = open('answers.txt', 'r')
    answers = testanswers.read()
    answers = answers.split('\n')
    testanswers.close
    return answers

#Read test.txt file which stores the students answers
def readtest():
    testfile = open('test.txt', 'r')
    test = testfile.read()
    test = test.split('\n')
    testfile.close
    return test

#Compares one question to another and writes to a file.
def comparetests(test, answers):
    correct=[]
    incorrect=[]
    questions = len(test)
    student_answers = 0
    question_count = 1
    
    while student_answers < questions:
        answer_answer = answers[student_answers].split(' ')
        test_answer = test[student_answers].split(' ')
        if answer_answer[1] == test_answer[1]:
            correct.append(question_count)
        else:
            incorrect.append(question_count)
        student_answers += 1
        question_count += 1
    return correct, incorrect

#Takes the input and gives a pass or fail. Also displays the incorrect questions.
def grade(correct, incorrect):
    if len(correct) >= 15:
        print("You passed with:", len(correct), "correct and", len(incorrect), "incorrect.")
        print("Incorrect answers on questions:", incorrect)
    else:
        print("You failed with:", len(correct), "correct and", len(incorrect), "incorrect.")
        print("Incorrect answers on questions:", incorrect)

main()
