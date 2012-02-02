#!/usr/bin/python3

"""
All square roots are periodic when written as continued fractions and can be 
written in the form:

√N = a0 +     1
      a1 +     1
            a2 +     1
                  a3 + ... 
For example, let us consider √23:
√23 = 4 + √23 — 4 = 4 +   1    = 4 +     1 
                          1          1 + √23 – 3
                        √23—4                7
                        
If we continue we would get the following expansion:
√23 = 4 +     1
          1 +   1
              3 +     1
                    1 +    1
                         8 + ...


It can be seen that the sequence is repeating. For conciseness, we use the 
notation √23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats 
indefinitely.

The first ten continued fraction representations of (irrational) square roots 
are:

√2=[1;(2)], period=1
√3=[1;(1,2)], period=2
√5=[2;(4)], period=1
√6=[2;(2,4)], period=2
√7=[2;(1,1,1,4)], period=4
√8=[2;(1,4)], period=2
√10=[3;(6)], period=1
√11=[3;(3,6)], period=2
√12= [3;(2,6)], period=2
√13=[3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N ≤ 13, have an odd period.

How many continued fractions for N ≤ 10000 have an odd period?
"""

import cProfile
import math

def continuedFractionSolver(num):
    endterms = set()
    mn = 0
    dn = 1
    an = int(math.sqrt(num))
    if an * an == num: return 0
    period = 1
    while (mn,dn,an) not in endterms:
        endterms.add((mn,dn,an))
        mtemp = dn * an - mn
        dtemp = (num - mtemp*mtemp) // dn
        atemp = int((math.sqrt(num) + mtemp)) // dtemp
        mn, dn, an = mtemp, dtemp, atemp
        period += 1
        
    return period

def main():
    L = 10**4
    odd_period = 0
    for i in range(2, L+1):
        x = continuedFractionSolver(i)
        if x % 2 == 1: odd_period += 1
    
    print(odd_period)

if __name__ == '__main__':
    cProfile.run('main()')