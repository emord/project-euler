#!/usr/bin/python

"""

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import libeuler
import cProfile
import math

def main():
    temp = 600851475143
    primes = libeuler.primeNumGen(int(math.sqrt(temp)))
    
    for i in primes[::-1]:
        if temp % i == 0:
            print(i)
            break
            
        

if __name__ == '__main__':
    cProfile.run('main()')