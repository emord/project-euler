#!/usr/bin/python3

"""
In England the currency is made up of pound, £, and pence, p, and there are 
eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""

import cProfile

def main():
    result = 0
    for i in range(0,201,200):
        for j in range(0,201-i,100):
            for k in range(0,201-j-i,50):
                for l in range(0,201-k-j-i,20):
                    for m in range(0,201-l-k-j-i,10):
                        for n in range(0,201-m-l-k-j-i,5):
                            for o in range(0,201-n-m-l-k-j-i,2):
                                for p in range(0,201-o-n-m-l-k-j-i,1):
                                    if i+j+k+l+m+n+o+p == 200: result+=1
                                    
    print(result)
   
if __name__ == '__main__':
    cProfile.run('main()')