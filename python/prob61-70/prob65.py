#!/usr/bin/python3

"""
Hence the sequence of the first ten convergents for √2 are:
1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...

What is most surprising is that the important mathematical constant,
e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

The first ten terms in the sequence of convergents for e are:
2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent of the continued
fraction for e.
"""

import cProfile
from fractions import gcd

def main():
    fracs = [ 2 ]
    for i in range(1, 50):
        fracs.append(1)
        fracs.append(2*i)
        fracs.append(1)
        
    fracs = fracs[:100]
    fracs = fracs[::-1]
    frac = [fracs[0], 1]
    
    for x in fracs[1:]:
        frac = [x*frac[0] + frac[1], frac[0]]
        g = gcd(frac[0], frac[1])
        frac[0] //= g
        frac[1] //= g
        
    print(frac)
    print(sum([int(i) for i in str(frac[0])]))

if __name__ == '__main__':
    cProfile.run('main()')