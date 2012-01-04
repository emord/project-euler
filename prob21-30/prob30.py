#!/usr/bin/python3

"""
Surprisingly there are only three numbers that can be written as the sum of 
fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers 
of their digits.
"""

import cProfile

def fifthpowersum(num):
    lookup = [0, 1, 32, 243, 1024, 3125, 7776, 16807, 32768, 59049]
    result = 0
    temp = num
    
    while not temp % 10 == 0 or temp > 0:
        result = result + (lookup[temp % 10])
        temp = temp // 10
 
    if result == num:
        return True

    return False

def main():
    result = 0
    topbound = 6 * (9 ** 5)
    lowerbound = 1000
    
    for x in range(lowerbound, topbound):
        if fifthpowersum(x):
            result += x
        
    print(result)
   
if __name__ == '__main__':
    cProfile.run('main()')