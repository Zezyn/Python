#!usr/bin/python

#File Name: 
#Developer: Martin Hernandez
#Date: 
#E-mail: 7607920511m.h@gmail.com
#Description: In this problem you will re-create the classic race of the tortoise and the hare.
#You will use random-number generation to develop a simulation of this memorable event.

#Our contenders begin the race at "square 1" of 70 squares. Each square represents a possible
#position along the race course. The finish line is at square 70. The first contender to reach
#or pass square 70 is rewarded with a pail of fresh carrots and lettuce. The course weaves its
#way up the side of a slippery mountain, so occasionally the contenders lose ground.there is a
#clock that ticks once per second. With each tick of the clock, your program should adjust the
#position of the animals according to the following rules:
#Use variables to keep track of the positions of the animals (ie., position numbers are 1-70).
#Start each animal at position 1 (i.s., the "starting gate"). If an animal slips left before
#square 1, move the animal back to square 1.

#Generate the percentages in the preceding table by producing a random integer i in the range
#1<= i <= 10. For the tortoise, perform a "fast plod" when 1 <=i <= 5, a "slip" when 6 <=i <=7
#or a "slow plod" when 8<=i<=10. Use a similar technique to move the hare.

#Begin the race by printing

#BANG!!!!!
#AND THEY'RE OFF !!!!

#For each tick of the click (i.e., each repetition of a loop), print a 70-position line showing
#the letter T in the toroise's position and the letter H in the hare's position. Occasionally,
#the contenders land on the same square. In this case, the tortoise bites the hare, and your
#program should print OUCH!!! beginning at that position. All print positions other than the T,
#the H or the OUCH!!! (in case of a tie) should be blank.

#After printing each line, test if either animal has reached or passed square 70. If so, print
#the winner and terminate the simulation. If the tortoise wins, print TORTOISE WINS!!! YAY!!! If
#the hare wins, print Hare wins. Yawn. . .
#If both animals win on the same clock tick, you may want to favor the tortoise (the "underdog"),
#or you may want to print It's a tie. If neither animal wins, perform the loop again to simulate
#the next tick of the clock.

import random

def main():

while i <= 70

    path = 70

    Tortoise = 1
    Hare = 1
    fastplod = 3
    slip = -6
    slowplod = 1
    bighop = 9
    bigslip = -12
    smallhop = 1
    smallslip = -2
    
    i = random.randint(1, 10)
    print(i)
    if i < 1:
        Tortoise = 1
    elif i >= 1 and i <= 5:
        Tortoise = Tortoise + fastplod
    elif i >= 6 and i <=7:
        Tortoise = Tortoise + slip
    elif i >= 8 and i <= 10:
        Tortoise = Tortoise + slowplod
        Hare = Hare + smallhop
    
    elif Hare < 1:
        Hare = 1

main()
