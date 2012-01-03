#!/usr/bin/python3

"""
The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in 
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include 
leading zeros.)
"""

import cProfile

def main():
    result = [ ]
   
    for x in range(1, 1000001):
        numstr = str(x)
        if numstr == numstr[::-1]:
            numbin = bin(int(numstr))[2:]
            if numbin == numbin[::-1]:
                result.append(x)

    print(result)
    print(sum(result))

if __name__ == '__main__':
    cProfile.run('main()')