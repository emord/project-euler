#!/usr/bin/python3

"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); 
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its 
alphabetical position and adding these values we form a word value. For 
example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value 
is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file 
containing nearly two-thousand common English words, how many are triangle 
words?
"""

import cProfile

def triangleNumbers(n):
    result = [ ]
    for x in range(1, n):
        result.append(.5 * x * (x + 1))
    return result

def getords():
    y = dict()
    for x in range(65,65+27):
        y[chr(x)] = x-64
    return y

def main():
    result = 0
    triangleNums = set(triangleNumbers(100))
    ords = getords()
    f = open('prob42.dat')
    f = f.read()
    f = f.strip().split(',')

    for x in f:
        temp = 0
        for y in x[1:-1]: 
            temp += ords[y]
        if temp in triangleNums: 
            result += 1

    print(result)
   
if __name__ == '__main__':
    cProfile.run('main()')
