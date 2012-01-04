#!/usr/bin/python3

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import cProfile

def main():
    s = 1000
    for i in range(1, s):
        for j in range(i, s):
            k = s - i - j
            if i * i + j * j == k * k:
                print(i*j*k)
                return
                

if __name__ == '__main__':
    cProfile.run('main()')