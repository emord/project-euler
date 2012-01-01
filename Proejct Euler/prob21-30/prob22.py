#!/usr/bin/python3

"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file 
containing over five-thousand first names, begin by sorting it into alphabetical
order. Then working out the alphabetical value for each name, multiply this 
value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is 
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would 
obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

import cProfile

def main():
    result = 0
    f = open('names.txt').read().split(',')
    f.sort()
    for i in range(len(f)):
        temp = 0
        for j in f[i][1:-1]:
            temp += ord(j) - 64
        result += temp * (i + 1)
    print(result)
    
if __name__ == '__main__':
    cProfile.run('main()')
    