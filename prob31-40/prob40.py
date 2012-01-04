#!/usr/bin/python3

"""
An irrational decimal fraction is created by concatenating the positive
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the 
following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

import cProfile

def main():
   count = 1
   frac = ''
   result = 1

   while len(frac) < 1000000:
      frac += str(count)
      count += 1

   for x in range(7):
      result *= int(frac[10**x - 1])

   print(result)
   
if __name__ == '__main__':
    cProfile.run('main()')