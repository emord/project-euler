#!/usr/bin/python3
"""
The cube, 41063625 (345^3), can be permuted to produce two other cubes: 
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube 
which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are 
cube.
"""

import cProfile

def main():
    dictcubes = dict()
    for i in range(10**0,10**5):
        cube = i*i*i
        if str(sorted(str(cube))) not in dictcubes.keys():
            dictcubes[str(sorted(str(cube)))] = [1, i]
        else:
            dictcubes[str(sorted(str(cube)))][0] += 1
            if dictcubes[str(sorted(str(cube)))][0] == 5:
                print(dictcubes[str(sorted(str(cube)))][1]**3)
                break
            
if __name__ == '__main__':
    cProfile.run('main()')