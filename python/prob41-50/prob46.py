#!/usr/bin/python3

"""
It was proposed by Christian Goldbach that every odd composite number can be 
written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime 
and twice a square?
"""

import cProfile
import libeuler

def main():
    primes = libeuler.primeNumGen(10000)
    primeset = set(primes)
   
    for i in range(9, 10000, 2): # odd numbers
        if i in primeset: continue
        x = False
        for j in primes:
            if j > i: break
            for k in range(1,i-j):
                temp = j + 2 * k * k
                if temp == i:
                    x = True
                    break
                elif temp > i: break
            if x: break
        if not x:
            print(i)
            return
      
if __name__ == '__main__':
    cProfile.run('main()')