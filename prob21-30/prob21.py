#!/usr/bin/python3

"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n 
which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and 
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

import cProfile
import libeuler

def main():
    sumofdivisors = [ 0 ] * 10000
    result = 0
    
    for i in range(1, 10000):
        sumofdivisors[i] = sum(libeuler.getDivisors(i))
        
    for i in range(2, 10000):
        temp = sumofdivisors[i]
        if temp > 10000 or temp == i: continue
        if i == sumofdivisors[temp]: result += i
    
    print(result)
    
if __name__ == '__main__':
    cProfile.run('main()')