#!/usr/bin/python3

"""
It can be seen that the number, 125874, and its double, 251748, contain exactly 
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain
the same digits.
"""

import cProfile

def main():
    for x in range(1,1000000000):
        if (set(str(x)) == set(str(x*2)) == set(str(x*3)) == set(str(x*4)) == 
            set(str(x*5)) == set(str(x*6))):
            print(x)
            return

if __name__ == '__main__':
    cProfile.run('main()')