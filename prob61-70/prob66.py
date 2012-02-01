#!/usr/bin/python3

"""
Consider quadratic Diophantine equations of the form:

x2 – Dy2 = 1

For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.

It can be assumed that there are no solutions in positive integers when D is 
square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the 
following:

32 – 2×22 = 1
22 – 3×12 = 1
92 – 5×42 = 1
52 – 6×22 = 1
82 – 7×32 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is 
obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value
of x is obtained.
"""

# using Pell's equation

import cProfile
import math
from fractions import gcd

def continuedFractionSolver(num, numto):
    mn = 0
    dn = 1
    an = int(math.sqrt(num))
    if an * an == num: return 0
    result = [ an ]
    for i in range(numto):
        mtemp = dn * an - mn
        dtemp = (num - mtemp*mtemp) // dn
        atemp = int((math.sqrt(num) + mtemp)) // dtemp
        mn, dn, an = mtemp, dtemp, atemp
        result.append(an)
        
    return result

def continuedFractionReturner(coeffList):
    coeffList.reverse()
    frac = (coeffList[0], 1)
    for i in coeffList[1:]:
        frac = (i * frac[0] + frac[1], frac[0])
        g = gcd(frac[0], frac[1])
        if g != 1: frac = (frac[0]//g, frac[1]//g)
        
    return frac
        
def main():
    result = 0
    blah = 0
    squares = set([i*i for i in range(10**3)])
    nums = [i for i in range(2, 1001) if i not in squares]
    for i in nums:
        if i % 5 == 0: print(i)
        for j in range(1, 100):
            z = continuedFractionSolver(i, j)
            x, y = continuedFractionReturner(z)
            if x * x - i * y * y == 1:
                if x > result:
                    blah = i
                    result = x
                break
        
    print(result, blah)
        
if __name__ == '__main__':
    cProfile.run('main()')