#!/usr/bin/python3

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import cProfile
import libeuler

def main():
    print(sum(libeuler.primeNumGen(2*10**6)))

if __name__ == '__main__':
    cProfile.run('main()')