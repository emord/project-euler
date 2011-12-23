#!/usr/bin/python3

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the 
numbers from 1 to 20?
"""

import cProfile

def main():
    result = 20
    notdivis = True
    
    while notdivis:
        temp = True
        for i in range(11,21):
            if result % i != 0:
                temp = False
                break
        if temp:
            break
        else: result += 20
        
    print(result)
    
if __name__ == '__main__':
    cProfile.run('main()')