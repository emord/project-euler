#!/usr/bin/python3

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that 
the 6th prime is 13.

What is the 10 001st prime number?
"""

import cProfile
import libeuler

def main():
    print(libeuler.primeNumGenByTerm(10001)[-1])

if __name__ == '__main__':
    cProfile.run('main()')