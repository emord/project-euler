#!/usr/bin/python3

"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial
of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

import cProfile
from math import factorial

def main():
    result = 0
    facts = [factorial(0), factorial(1), factorial(2), factorial(3),
             factorial(4), factorial(5), factorial(6), factorial(7),
             factorial(8), factorial(9) ]
    for x in range(100, 1000):
        factsum = facts[x//100] + facts[(x//10)%10] + facts[x%10]
        if factsum == x: result += x

    for x in range(1000, 10000):
        factsum = facts[(x//1000)%10] + facts[(x//100)%10] + facts[(x//10)%10] 
        factsum += facts[x%10]
        if factsum == x: result += x

    for x in range(10000, 100000):
        factsum = facts[(x//10000)%10] + facts[(x//1000)%10] 
        factsum += facts[(x//100)%10] + facts[(x//10)%10] + facts[x%10]
        if factsum == x: result += x
        
    print(result)

if __name__ == '__main__':
    cProfile.run('main()')