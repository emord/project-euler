"""
Various algorithms I have found useful for solving Project Euler problems.
"""

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

def primeNumGen(maxnum):
    nums = [True] * (int(maxnum) + 1)
    nums[0] = False
    nums[1] = False
    
    for i in range(2,int(maxnum)+1):
        if nums[i]:
            temp = i + i
            while temp < int(maxnum)+1:
                nums[temp] = False
                temp += i
    
    return [i for i in range(int(maxnum)+1) if nums[i]]

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
    