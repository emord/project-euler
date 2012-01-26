#!/usr/bin/python3

"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and
HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of
size, we get:

   1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
   5/7, 3/4, 4/5, 5/6, 6/7, 7/8

   It can be seen that 2/5 is the fraction immediately to the left of 3/7.

   By listing the set of reduced proper fractions for d ≤ 1,000,000 in
   ascending order of size, find the numerator of the fraction immediately to
   the left of 3/7.
"""

from fractions import Fraction, gcd
import cProfile

def main():
   frac37 = Fraction(3,7)
   dec37 = 3/7
   before37 = 428/999
   fracbefore37 = Fraction(428,999)
   for d in range(10**6-5, 10**6+1):
      for n in range(int(d/3), int(d/2)):
         temp = n/d
         fractemp = Fraction(n,d)
         if temp > dec37:
            break
         elif temp < before37:
            continue
         if temp > before37 and temp < dec37:
            before37 = temp
            fracbefore37 = fractemp
         elif temp == before37 or temp == dec37:
            if fractemp > fracbefore37 and fractemp < frac37:
               before37 = temp
               fracbefore37 = Fraction(1,d)

   print(fracbefore37)
   print(before37)


if __name__ == "__main__":
   cProfile.run('main()')
