#!/usr/bin/python3

"""
Comparing two numbers written in index form like 211 and 37 is not difficult, as
any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382518061 > 519432525806 would be much more 
difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file 
containing one thousand lines with a base/exponent pair on each line, determine 
which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given
above.
"""

import cProfile
from multiprocessing import Queue, Process
import math

def worker(lines, out_q, lineNum):
    maxim = -28
    i = lineNum
    result = i
    for line in lines:
        i += 1
        x = line.split(',')
        y = int(x[1]) * math.log10(int(x[0]))
        if y > maxim: 
            maxim = y
            result = i
        
    out_q.put(result)

def main():
    f = open('prob99.dat').readlines()
    a = Queue()
    b = Queue()
    i = Process(target=worker, args=(f[:len(f)//2], a, 0))
    j = Process(target=worker, args=(f[len(f)//2:], b, len(f)//2))
    i.start()
    j.start()
    i.join()
    j.join()
            
    linenum = a.get()
    maxim = int(f[linenum].split(',')[1]) * math.log10(int(f[linenum].split(',')[0]))

    m = b.get()
    y     = int(f[m].split(',')[1]) * math.log10(int(f[m].split(',')[0]))
    if y > maxim: 
        maxim = y
        linenum = m 

    print(linenum)

if __name__ == '__main__':
    cProfile.run('main()')
