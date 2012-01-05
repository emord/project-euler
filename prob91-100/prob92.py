#!/usr/bin/python3

"""
A number chain is created by continuously adding the square of the digits in a 
number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless 
loop. What is most amazing is that EVERY starting number will eventually arrive 
at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

import cProfile

def chainAt89(num):
    temp = num
   
    while temp != 89 and temp != 1:
        x = list(str(temp))
        temp = 0
        for y in x:
            temp += int(y)**2
         
    if temp == 89: return True
    else: return False
   
def main():
    squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    result = 0
    x = [False] * 577
    for i in range(1,577):
        if chainAt89(i):
            result += 1
            x[i] = True
         
    for i in range(577,10**7):
        temp = 0
        while i:
            j = i%10
            i = i//10
            temp += squares[j]
            
        if x[temp]:
            result += 1
   
    print(result)

if __name__ == '__main__':
    cProfile.run('main()')