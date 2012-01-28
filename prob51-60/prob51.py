#!/usr/bin/python3

"""
By replacing the 1st digit of *3, it turns out that six of the nine possible 
values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit 
number is the first example having seven primes among the ten generated numbers,
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. 
Consequently 56003, being the first member of this family, is the smallest prime
with this property.

Find the smallest prime which, by replacing part of the number (not necessarily 
adjacent digits) with the same digit, is part of an eight prime value family.
"""

import cProfile
import libeuler

def numsToCheck(prime, num):
    strnum = str(prime).split(str(num))
    result = [ ]
    for i in range(10):
        result.append(str(i).join(strnum))
    return result

def main():
    primes = libeuler.primeNumGen(10**6)
    setprimes = set(primes)
    for prime in primes:
        for i in range(10):
            temp = 0
            if str(i) not in str(prime): continue
            primesToCheck = numsToCheck(prime, i)
            for j in primesToCheck:
                if int(j) in setprimes and int(j) > prime:
                    temp += 1
            if temp == 7:
                print(prime)
                return

if __name__ == '__main__':
    cProfile.run('main()')