#!/usr/bin/python3

"""
The first two consecutive numbers to have two distinct prime factors are:

   14 = 2 × 7
   15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors
are:

      644 = 2² × 7 × 23
      645 = 3 × 5 × 43
      646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct primes
factors. What is the first of these numbers?
"""

import cProfile
import libeuler
import math

def main():
    numfactors = 0
    consecprimes = 0
    index = 1
    primes = libeuler.primeNumGen(10**6)
    primeset = set(primes)

    while consecprimes < 4:
        if index in primeset:
            index += 1
            consecprimes = 0
            continue
        numfactors = len(set(libeuler.primeFactorization(index, primes)))
        if numfactors == 4:
            consecprimes += 1
        else:
            consecprimes = 0
        index += 1

    print(index-4)
   
if __name__ == '__main__':
    cProfile.run('main()')