#Problem Statement: "You are given a standard deck of cards with 26 black cards and 26 red cards. You're now going to play a game: 
#in every round, you can take one of two actions: you can stop playing, or you can draw another card. If you draw another card and 
#it's red, you get one dollar. If you draw another card and it's black, you lose one dollar. What is the expected value of this game?"

import math

black = int(input('How many black cards are there?\n'))
red = int(input('How many red cards are there?\n'))

def expected_value(b, r):
    if (b == 0 and r == 0):
        return 0
    else:
        return max(0, b / (r + b) * (-1 + expected_value(b-1, r)) + r / (r + b) * (1 + expected_value(b, r-1)))

print(expected_value(black, red))
