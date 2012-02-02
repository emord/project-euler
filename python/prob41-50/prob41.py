#!/usr/bin/python3

"""
We shall say that an n-digit number is pandigital if it makes use of all the 
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is 
also prime.

What is the largest n-digit pandigital prime that exists?
"""

import cProfile
import libeuler

def isPandigital(num):
    x = set(str(num))
   
    for i in range(1, len(x)+1):
        if str(i) not in x:
            return False
    return True
   
def main():
    result = 0
    primes = libeuler.primeNumGen(7654321)
   
    for i in primes[::-1]:
        if len(set(str(i))) == len(str(i)) and isPandigital(i):
            result = i
            break
   
    print(result)

if __name__ == '__main__':
    cProfile.run('main()')