#!/usr/bin/python

"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases 
by 3330, is unusual in two ways: (i) each of the three terms are prime, and, 
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this 
sequence?
"""

import cProfile
import libeuler

def all_perms(str):
    result = [ ]
    if len(str) <=1:
        return str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                result.append(perm[:i] + str[0:1] + perm[i:])
    return list(set(result))
                
def main():
    primes = libeuler.primeNumGen(10000)
    primes = [x for x in primes if len(str(x)) == 4]
    primeset = set(primes)
    used = [ ]
   
    for i in primes:
        if (i + 3330) in primeset and (i + 6660) in primeset:
            perms = all_perms(str(i))
            if str(i+3330) in perms and str(i+6660) in perms:
                print(i, i+3330, i+6660)

if __name__ == '__main__':
    cProfile.run('main()')