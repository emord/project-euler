#!/usr/bin/python3

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we 
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import math
import cProfile

def multiplesOfN(maxnum, N):
    return [ i*N for i in range(1,math.ceil(maxnum/N)) ]

def main():
    # multiples of five
    mult5 = multiplesOfN(1000, 5)
    mult3 = multiplesOfN(1000, 3)
    mult15 = multiplesOfN(1000, 15)
    
    #result = set(mult5 + mult3)
    # OR
    result = sum(mult5) + sum(mult3) - sum(mult15)
    
    print(result)

if __name__ == "__main__":
    cProfile.run('main()')
    