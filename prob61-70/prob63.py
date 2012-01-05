#!/usr/bin/python3

"""
The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit 
number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

import cProfile

def main():
    result = 0
    for i in range(1,10):
        for j in range(1,100):
            if len(str(i**j)) == j:
                print(i**j)
                result += 1
            elif len(str(i**j)) > j:
                break
            
    print(result)

if __name__ == '__main__':
    cProfile.run('main()')