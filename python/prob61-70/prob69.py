#!/usr/bin/python3

"""
Euler's Totient function, φ(n) [sometimes called the phi function], is used to 
determine the number of numbers less than n which are relatively prime to n. For
example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to
nine, φ(9)=6.

n     Relatively Prime     φ(n)     n/φ(n)
2     1                    1         2
3     1,2                  2        1.5
4     1,3                  2         2
5     1,2,3,4              4        1.25
6     1,5                  2         3
7     1,2,3,4,5,6          6        1.1666...
8     1,3,5,7              4         2
9     1,2,4,5,7,8          6        1.5
10     1,3,7,9             4        2.5

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
"""

import cProfile
import libeuler
from multiprocessing import Process, Queue

def worker(spread, primes, out_q):
    result = 0
    maxratio = 0.001
    for i in spread:
        temp = i
        for j in set(libeuler.primeFactorization(i, primes)):
            temp *= (1 - 1/j)
        if i / temp > maxratio:
            maxratio = i/temp
            result = i
            
    out_q.put((maxratio, result))
    
def main():
    limit = 10**6
    primes = libeuler.primeNumGen(limit)
    
    a = Queue()
    b = Queue()
    c = Queue()
    i = Process(target=worker, args=(range(2, limit+1, 3), primes, a))
    j = Process(target=worker, args=(range(3, limit+1, 3), primes, b))
    k = Process(target=worker, args=(range(4, limit+1, 3), primes, c))
    i.start()
    j.start()
    k.start()
    i.join()
    j.join()
    k.join()
    
    print(a.get())
    print(b.get())
    print(c.get())
    
if __name__ == '__main__':
    cProfile.run('main()')