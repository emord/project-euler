#!/usr/bin/python3

"""
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural 
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.
"""

import cProfile
import multiprocessing

def sumOfSquares(num, out_q):
    result = 0
    for i in range(1, num):
        result += i*i
    out_q.put(result)
#    out_q.put(sum([i*i for i in range(1, num)]))

def squareOfSum(num, out_q):
    #out_q.put(sum([i for i in range(1,num)]) ** 2)
    out_q.put(((num*(num-1))//2) * ((num*(num-1))//2))

def main():
    n = 101
    #a =  sumOfSquares(n)
    #b = squareOfSum(n)
    
    a = multiprocessing.Queue()
    b = multiprocessing.Queue()
    
    x = multiprocessing.Process(target=sumOfSquares, args=(n, a))
    y = multiprocessing.Process(target=squareOfSum,  args=(n, b))
    x.start()
    y.start()
    x.join()
    y.join()
    
    print(b.get()- a.get())

if __name__ == '__main__':
    cProfile.run('main()')
