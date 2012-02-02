#!/usr/bin/python3

"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in 
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 
letters. The use of "and" when writing out numbers is in compliance with British
usage.
"""

import cProfile


# thousand has 8 letters
# hundred has 7 letters

def numletters(num):
    ones  = [ 3, 3, 5, 4, 4, 3, 5, 5, 4 ]
    tens  = [ 3, 6, 6, 5, 5, 5, 7, 6, 6 ]
    teens = [ 6, 6, 8, 8, 7, 7, 9, 8, 8 ]

    temp = num
    result = 0
    if temp >= 1000:
        result += 8
        temp1 = temp // 1000
        temp = temp % 1000
        result += numletters(temp1)

    if temp >= 100:
        if not temp % 100 == 0:
            result += 3 # for and
        result += 7
        temp1 = temp // 100
        temp = temp % 100
        result += numletters(temp1)
   
    if temp > 10 and temp < 20:
        result += teens[temp%10 - 1]
    else:
        if temp % 10 > 0:
            result += ones[temp%10 - 1]
        if temp >= 10:
            result += tens[temp//10 - 1]

    return result
   
def main():
    result = [ ]
    limit = 1000 

    for x in range(1, limit + 1):
        result.append(numletters(x))

    print(sum(result))

if __name__ == '__main__':
    cProfile.run('main()')