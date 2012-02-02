#!/usr/bin/python3

"""
We shall say that an n-digit number is pandigital if it makes use of all the 
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through
5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing 
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can 
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only 
include it once in your sum.
"""

import cProfile

def main():
    numset = set()
    result = 0
   
    for i in range(1, 100):
        for j in range(100, 10000):
            stringprod = str(i) + str(j) + str(i*j)
            if '0' in stringprod or len(stringprod) != 9: continue
            if len(set(stringprod)) == 9:
                numset.add(i*j)
                
    for x in numset:
        result += x
        print(x)
      
    print(result)

if __name__ == '__main__':
    cProfile.run('main()')