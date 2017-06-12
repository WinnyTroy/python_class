# Name: WInnie Kiragu
# Section: Internship
# homework_2.py

##### Template for Homework 2, exercises 3.1-3.4  ######


# **********  Exercise 3.1 ********** 


import random
import sys
import math
import unittest

moves = ['r', 'p', 's']
player_wins = ['pr', 'sp', 'rs']

player2_move = random.choice(moves)
player1_move = sys.argv[1]



def player1_choice_rock():
    if player1_move == 'r':
        return "You tie Bitch"
    elif player2_move == 'p':
        return "You win Sensei"
    else:
        return "Go home!"


def player1_choice_paper():
    if player1_move == 'r':
        return "Go home!"
    elif player2_move == 'p':
        return "You tie Bitch"
    else:
        return "You win Sensei"


def player1_choice_scissors():
    if player1_move == 'r':
        return "You win Sensei"
    elif player2_move == 'p':
        return "Go home!"
    else:
        return "You tie Bitch"


if player2_move == 'r':
    print player1_choice_rock()
elif player2_move == 'p':
    print player1_choice_paper()
else:
    print player1_choice_scissors()

# Test Cases for Exercise 3.1
##### YOUR CODE HERE #####

# *********** Exercise 3.2 ***********
## 1 - multadd function
def multiadd(a, b, c):
    return a * b + c

## 2 - Equations

angle_test = multiadd(math.cos(math.pi / 4), 0.5, math.sin(math.pi / 4))
print "sin(pi/4) + cos(pi/4)/2 is:"
print angle_test

ceiling_test = math.ceil(276 / 19.0) + 2 * math.log(12, 7)
print "ceiling(276/19) + 2 log_7(12) is:"
print ceiling_test

## 3 - yikes function
def yikes(x):
    eToNegX = math.exp(-x)
    sqrtTerm = math.sqrt(1 - eToNegX)
    return multiadd(x, eToNegX, sqrtTerm)


print "yikes(5) is " + str(yikes(5))


# Test Cases
# x = 5
# print "yikes(5) =", yikes(x)

# ********** Exercise 3.3 **********

## 1 - rand_divis_3 function


import random
import unittest


def rand_divis_3():
    num = random.randint(0, 100)

    print "Number selected is: ", num

    if num % 3 == 0:
        print "  True - Randomly selected number is divisible by 3"
    else:
        print " False - Randomly selected number is not divisible by 3"


rand_divis_3()
# Test Cases
##### YOUR CODE HERE #####

## 2 - roll_dice function - remember that a die's lowest number is 1;
                            #its highest is the number of sides it has

def roll_dice(sides, dice):
    for die in range(dice):
        num = random.randint(1, sides)
        print "Dice #" + str(die + 1) + " rolled a " + str(num) + "."


roll_dice(4, 2)


# Test Cases
##### YOUR CODE HERE #####                            

