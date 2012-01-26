#!/usr/bin/python3

"""
The first known prime found to exceed one million digits was discovered in 
1999, and is a Mersenne prime of the form 2**6972593−1; it contains exactly 
2,098,960 digits. Subsequently other Mersenne primes, of the form 2p−1, have 
been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 
2,357,207 digits: 28433×2**7830457+1.

Find the last ten digits of this prime number.
"""

import cProfile

def main():
    num = 0
    result = 1 
    mod = 10 ** 10
    power = 2 ** 10000 % mod
   
    while num < 7830000:
        result = result * power % mod 

        num += 10000

    result = result * 2 ** 457 % mod

    result = result * 28433 % mod

    result += 1

    print(result % mod)

if __name__ == '__main__':
    cProfile.run('main()')
