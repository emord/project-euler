#!/usr/bin/python3

"""
Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and 
each line adding to nine.

Working clockwise, and starting from the group of three with the numerically 
lowest external node (4,3,2 in this example), each solution can be described 
uniquely. For example, the above solution can be described by the set: 
4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 
9, 10, 11, and 12. There are eight solutions in total.

Total    Solution Set
9    4,2,3; 5,3,1; 6,1,2
9    4,3,2; 6,2,1; 5,1,3
10    2,3,5; 4,5,1; 6,1,3
10    2,5,3; 6,3,1; 4,1,5
11    1,4,6; 3,6,2; 5,2,4
11    1,6,4; 5,4,2; 3,2,6
12    1,5,6; 2,6,4; 3,4,5
12    1,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings; the maximum 
string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to 
form 16- and 17-digit strings. What is the maximum 16-digit string for a "magic"
5-gon ring?
                a1
                    a6      a2
                a10     a7
            a5
                 a9    a8    a3
                 
                  a4
"""

import cProfile

def main():
    result = [ ]
    for a1 in range(1, 7):
        for a2 in range(a1, 11):
            if a2 == a1: continue
            for a3 in range(a1, 11):
                if a3 == a2 or a3 == a1: continue
                for a4 in range(a1, 11):
                    if a4 == a3 or a4 == a2 or a4 == a1: continue
                    for a5 in range(a1, 11):
                        if a5 == a4 or a5 == a3 or a5 == a2 or a5 == a1: 
                            continue
                        for a6 in range(1, 10):
                            if (a6 == a5 or a6 == a4 or a6 == a3 or 
                                a6 == a2 or a6 == a1): 
                                continue
                            for a7 in range(1, 10):
                                if (a7 == a6 or a7 == a5 or a7 == a4 or 
                                    a7 == a3 or a7 == a2 or a7 == a1):
                                     continue
                                for a8 in range(1,10):
                                    if (a8 == a7 or a8 == a6 or a8 == a5 or 
                                        a8 == a4 or a8 == a3 or a8 == a2 or 
                                        a8 == a1): 
                                        continue
                                    for a9 in range(1, 10):
                                        if (a9 == a8 or a9 == a7 or a9 == a6 or 
                                            a9 == a5 or a9 == a4 or a9 == a3 or 
                                            a9 == a2 or a9 == a1): 
                                            continue
                                        for a10 in range(1, 10):
                                            if (a10 == a9 or a10 == a8 or 
                                                a10 == a7 or a10 == a6 or 
                                                a10 == a5 or a10 == a4 or 
                                                a10 == a3 or a10 == a2 or 
                                                a10 == a1): 
                                                continue
                                            if (a1+a6+a7 == a2+a7+a8 == 
                                                a3+a8+a9 == a4+a9+a10 == 
                                                a5+a10+a6):
                                                result.append(int(str(a1)+str(a6)+str(a7)+
                                                                  str(a2)+str(a7)+str(a8)+
                                                                  str(a3)+str(a8)+str(a9)+
                                                                  str(a4)+str(a9)+str(a10)+
                                                                  str(a5)+str(a10)+str(a6)))

    print(max(result))
    
if __name__ == '__main__':
    cProfile.run('main()')