#!/usr/bin/python3
"""
The number 145 is well known for the property that the sum of the factorial of 
its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers
that link back to 169; it turns out that there are only three such loops that 
exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get 
stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest 
non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty
non-repeating terms?
"""

import cProfile

def digitFactorial(num):
    facts = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    result = 0
    for i in str(num):
        result += facts[int(i)]
        
    return result
        
def main():
    result = 0
    numsdict  = dict()
    keysset   = set()
    for i in range(1,10**6):
        temp = 0
        num = i
        x = set()
        while num not in keysset and num not in x:
            x.add(num)
            num = digitFactorial(num)
            temp += 1
        if num in keysset: 
            temp += numsdict[num]
        numsdict[i] = temp
        keysset.add(i)
        if temp == 60: result += 1
    
    print(result)

if __name__ == '__main__':
    cProfile.run('main()')