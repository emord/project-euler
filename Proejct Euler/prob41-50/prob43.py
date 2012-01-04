#!/usr/bin/python

"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of 
each of the digits 0 to 9 in some order, but it also has a rather interesting 
sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note 
the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

import cProfile

def pandigitalGen():
    result = [ ]
    nums = set()
    for i in range(1,10):
        nums.add(i)
        for j in range(10):
            if j in nums: continue
            nums.add(j)
            for k in range(10):
                if k in nums: continue
                nums.add(k)
                for l in [0,2,4,6,8]:
                    if l in nums: continue
                    nums.add(l)
                    for m in range(10):
                        if m in nums: continue
                        if (k+l+m) % 3 != 0: continue
                        nums.add(m)
                        for n in [0, 5]:
                            if n in nums: continue
                            nums.add(n)
                            for o in range(10):
                                if o in nums: continue
                                if int(str(m)+str(n)+str(o)) % 7 != 0: continue
                                nums.add(o)
                                for p in range(10):
                                    if p in nums: continue
                                    if int(str(n)+str(o)+str(p)) % 11 != 0: continue
                                    nums.add(p)
                                    for q in range(10):
                                        if q in nums: continue
                                        if int(str(o)+str(p)+str(q)) % 13 != 0: continue
                                        nums.add(q)
                                        for r in range(10):
                                            if r in nums: continue
                                            if int(str(p)+str(q)+str(r)) % 17 != 0: continue
                                            result.append(int(str(i) + str(j) + str(k) + str(l) + str(m) + str(n) + str(o) + str(p) + str(q) + str(r)))
                                        nums.remove(q)
                                    nums.remove(p)
                                nums.remove(o)
                            nums.remove(n)
                        nums.remove(m)
                    nums.remove(l)
                nums.remove(k)
            nums.remove(j)
        nums.remove(i)
                  
    return result

def main():
    print(sum(pandigitalGen()))
   
if __name__ == '__main__':
    cProfile.run('main()')