#!/usr/bin/python3

"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in 
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is 
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than 
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, 
find the value of the denominator.
"""

import cProfile

def main():
   num = 0
   nums = [ ] 

   for firsttop in range(1, 10):
      for lastbottom in range(firsttop, 10):
         common = 1
         while num < 4 and common < 10: 
            unsimplified = (firsttop*10 + common) / (common*10 + lastbottom)
            simplified = firsttop / lastbottom
            if unsimplified == simplified and not simplified == 1:
               print(str(firsttop) + str(common) + '/' + str(common) + str(lastbottom))
               num += 1
               nums.append(simplified)
            common += 1

   product = 1
   for n in nums:
      product *= n

   print(product)

if __name__ == '__main__':
    cProfile.run('main()')