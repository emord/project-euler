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
    nums = [ [i, True] for i in range(2, maxnum + 1)]
    
    for i in range(len(nums)):
        if nums[i][1]:
            j = i + i + 2
            while j < len(nums):
                nums[j][1] = False
                j += i + 2
        else: continue
        
    return [i[0] for i in nums if i[1]]

def isPalindrome(blah):
    return str(blah) == str(blah)[::-1]