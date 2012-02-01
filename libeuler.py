"""
Various algorithms I have found useful for solving Project Euler problems.
"""

import math
from fractions import gcd

def fibonacci(term=None, maxnum=None):
    result = [ 0, 1]
    a = 0
    b = 1
    if type(term) is int:
        for i in range(3, term+1):
            result.append(a+b)
            a = b
            b = result[-1]
    elif type(maxnum) is int:
        while b <= maxnum:
            result.append(a+b)
            a = b
            b = result[-1]
        result.pop() # the last number is past the threshold
    else: raise TypeError
    
    return result

#stolen off wikipedia
def primeNumGen(limit):
    # creates list of numbers to limit
    candidates = list(range(limit + 1))
    # we only have to check to the sqrt of the limit
    fin = int(limit**0.5)

    for i in range(2, fin + 1):
        # if the candidate has been assigned None already
        if not candidates[i]:
            continue

        # selects a list of multiples of i
        # first i selects 2 * i
        # second i says to select every ith term
        # it then assigns a list of None to that list
        candidates[2*i::i] = [None] * (limit//i - 1)

    # starts at 2 b/c it is first prime and returns i if it is not None
    return [i for i in candidates[2:] if i]

def primeNumGenByTerm(term):
    #should find better formula than having a magic number
    primes = primeNumGen(12*term)
    num = 12 * term + 1
    
    while len(primes) < term:
        temp = True
        for i in primes:
            if num % i == 0:
                temp = False
                break
            
        if temp: primes.append(num)
        num += 2
    
    return primes[:term]

def isPalindrome(blah):
    return str(blah) == str(blah)[::-1]

def primeFactorization(num, primes=None):
    if type(primes) is not list:
        primes = primeNumGen(num)
        
    factors = [ ]
    i = 0
    while num != 1:
        if num % primes[i] == 0:
            factors.append(primes[i])
            num //= primes[i]
            continue
        else:
            i += 1
            continue
    
    return factors

def getNumDivisors(num, primes=None):
    factors = primeFactorization(num, primes)
    factordict = dict()
    result = 1
    
    for x in set(factors):
        factordict[x] = 0
    for i in factors:
        factordict[i] += 1
    for x in factordict.values():
        result *= (x+1)
        
    return result
    
def getDivisors(num):
    divisors = [1]
    
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            divisors.append(i)
            if num/i != i:
                divisors.append(num//i)
            
    return divisors

def isPrime(num):
    if num % 2 == 0: return False
    for i in range(3, int(math.sqrt(num)), 2):
        if num % i == 0: return False
    return True

def relativelyPrime(num):
    result = [ 1 ]
    for i in range(2, num):
        if gcd(i, num) == 1: result.append(num)
        
    return result