#!/usr/bin/python3

"""
If p is the perimeter of a right angle triangle with integral length sides, 
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximized?
"""

import cProfile
import math

def main():
    blah = dict()
    max = 0
    key = 0
   
    for i in range(0, 500):
        for j in range(i+1, 500):
            c = math.sqrt(j*j + i*i)
            if c+i+j in blah.keys():
                blah[c+i+j] += 1
            else: blah[c+i+j] = 1
   
    for key,value in blah.items():
        if value > max:
            max = value
            num = key
         
    print(str(max) + " " + str(num))
   
if __name__ == '__main__':
    cProfile.run('main()')