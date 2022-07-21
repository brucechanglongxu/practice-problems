import math

black = int(input('How many black cards are there?\n'))
red = int(input('How many red cards are there?\n'))

def expected_value(b, r):
    if (b == 0 and r == 0):
        return 0
    else:
        return max(0, b / (r + b) * (-1 + expected_value(b-1, r)) + r / (r + b) * (1 + expected_value(b, r-1)))

print(expected_value(black, red))
