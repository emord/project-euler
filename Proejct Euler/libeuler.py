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
    nums = [True] * maxnum
    nums[0] = False
    nums[1] = False
    
    for i in range(2,maxnum):
        if nums[i]:
            temp = i + i
            while temp < maxnum:
                nums[temp] = False
                temp += i
    
    return [i for i in range(maxnum) if nums[i]]

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