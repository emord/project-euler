#!/usr/bin/python3

"""
A palindromic number reads the same both ways. The largest palindrome made from 
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import cProfile
import libeuler

def main():
    result = 0
    for i in range(999, 100, -1):
        for j in range(i, 100, -1):
            temp = i*j
            if temp < result: break
            if libeuler.isPalindrome(temp):
                if temp > result: result = temp
                break
            
    print(result)
            

if __name__ == '__main__':
    cProfile.run('main()')