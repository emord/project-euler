#!/usr/bin/python3

"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes 
and concatenating them in any order the result will always be prime. For 
example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four 
primes, 792, represents the lowest sum for a set of four primes with this 
property.

Find the lowest sum for a set of five primes for which any two primes 
concatenate to produce another prime.
"""

import cProfile
import libeuler

def validPair(primes, maxprime, p1, p2):
    x = int(p1 + p2)
    y = int(p2 + p1)
    if x > maxprime: 
        if not libeuler.isPrime(x): return False
    else:
        if x not in primes: return False
    if y > maxprime: 
        if not libeuler.isPrime(y): return False
    else:
        if y not in primes: return False
        
    return True
    

def main():
    primes = libeuler.primeNumGen(10**6)
    shortprimes = libeuler.primeNumGen(10**4)
    priLen = len(shortprimes)
    setprimes = set(primes)
    maxprime = primes[-1]
    blah = 99999999999
    
    for i in range(priLen):
        ii = str(primes[i])
        for j in range(i+1, priLen):
            jj = str(primes[j])
            if not validPair(setprimes, maxprime, ii, jj):
                continue
            for k in range(j+1, priLen):
                kk = str(primes[k])
                if (not validPair(setprimes, maxprime, ii, kk) or
                   not validPair(setprimes, maxprime, jj, kk)):
                    continue
                for l in range(k+1, priLen):
                    ll = str(primes[l])
                    if (not validPair(setprimes, maxprime, ii, ll) or
                       not validPair(setprimes, maxprime, jj, ll) or
                       not  validPair(setprimes, maxprime, kk, ll)):
                        continue
                    for m in range(l+1, priLen):
                        mm = str(primes[m])
                        if (not validPair(setprimes, maxprime, ii, mm) or
                           not validPair(setprimes, maxprime, jj, mm) or
                           not validPair(setprimes, maxprime, kk, mm) or
                           not  validPair(setprimes, maxprime, ll, mm)):
                            continue
                        print(ii, jj, kk, ll, mm)
                        if blah > primes[i] + primes[j] + primes[k] + primes[l] + primes[m]: 
                            blah = primes[i]+primes[j]+primes[k]+primes[l]+primes[m]
                            
    print(blah)

if __name__ == '__main__':
    cProfile.run('main()')