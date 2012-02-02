#!/usr/bin/python3

"""
A googol (10^100) is a massive number: one followed by one-hundred zeros; 
100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite
their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the 
maximum digital sum?
"""

import cProfile
import math

def main():
    maxnum = 0

    for a in range(1,100):
        if a % 10 == 0: continue
        for b in range(1,100):
            temp = sum([int(i) for i in str(a**b)])
            if temp > maxnum:
                maxnum = temp

    print(maxnum)

if __name__ == '__main__':
    cProfile.run('main()')