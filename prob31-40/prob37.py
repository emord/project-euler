#!/usr/bin/python3

"""
The number 3797 has an interesting property. Being prime itself, it is possible 
to continuously remove digits from left to right, and remain prime at each 
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 
3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to 
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

import cProfile
import libeuler

def main():
    primes = libeuler.primeNumGen(1000000)
    setprimes = set(primes)
    result = [ ]
    
    # cant be truncatable
    primes.remove(2)
    primes.remove(3)
    primes.remove(5)
    primes.remove(7)
    
    for prime in primes:
        truncable = True
        for x in range(1, len(str(prime))):
            if int(str(prime)[x:]) in setprimes:
                if int(str(prime)[:x]) in setprimes:
                   continue
            truncable = False
            break
        if truncable: result.append(prime)
        
    print(result)
    print(sum(result))
            

if __name__ == '__main__':
    cProfile.run('main()')