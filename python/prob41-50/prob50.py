#!/usr/bin/python3

"""
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below 
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, 
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most 
consecutive primes?
"""

import cProfile
import libeuler

def main():
    primes = libeuler.primeNumGen(10**6)
    setprimes = set(primes)
    maxconnums = 0
    num = 0
   
    for i in range(0, len(primes)):
        if maxconnums > len(primes)-i: break
        temp = primes[i]
        added = 1
        for j in range(i+1, len(primes)):
            temp += primes[j]
            added += 1
            if temp > 1000000: break
            if temp in setprimes and added > maxconnums:
                maxconnums = added
                num = temp
         
    print(maxconnums, num)
   
if __name__ == '__main__':
    cProfile.run('main()')