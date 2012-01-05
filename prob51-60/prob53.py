#!/usr/bin/python3

"""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,
nCr =    
n!
r!(n−r)!
   ,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater 
than one-million?
"""

import cProfile
import math

def main():
    factorials = [ ]
    for i in range(101):
        factorials.append(math.factorial(i))
    
    result = 0
    
    for n in range(1, 100+1):
        for r in range(0, n):
            if factorials[n] / (factorials[r] * factorials[n-r]) > 10**6:
                result += 1
   
    print(result)

if __name__ == '__main__':
    cProfile.run('main()')