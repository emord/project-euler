#!/usr/bin/python3

"""
The number, 197, is called a circular prime because all rotations of the 
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
73, 79, and 97.

How many circular primes are there below one million?
""" 

import cProfile
import libeuler

def iscircularprime(num, primes): 
   length = len(str(num))

   for x in range(length):
      temp2 = int(str(num)[x:] + str(num)[:x]) 
      if not temp2 in primes:
         return False
   
   return True

def main():
   count = 1 #because of 2
   primes = libeuler.primeNumGen(1000000)
   setprimes = set(primes)

   # takes out any primes that have an even digit in them
   finalprimes = [ ]
   for x in primes:
      blah = True
      for y in str(x):
         if int(y) % 2 == 0:
            blah = False
            break
      if blah:
         finalprimes.append(x)

   for x in finalprimes:
      if iscircularprime(x, setprimes):
         count += 1

   print(count)

if __name__ == '__main__':
   cProfile.run('main()')
