# Write a function that takes an unsigned integer and returns its hamming weight.

def  countSetBits(n):
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count
