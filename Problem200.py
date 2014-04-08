#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=200
Find the 200th prime-proof sqube containing the contiguous sub-string "200"
Problem 200
'''

'''
Notes on problem 200():
*These could be nicely refactored
*It be nice if there was an interator that could go over
pairs (p,q) such that p**2*q**3 is in order
There is some orders to this, it might be possible.
'''

from PE_primes import primesUpTo, factorize, isPrime
from itertools import combinations


def isPrimeProofsqubeEven(p, q):
    n = p ** 2 * q ** 3
    if "200" not in str(n):
        return False
    for i in range(1, 10, 2): # the last digit is odd
        if isPrime(int(str(n)[:-1] + str(i))):
            return False
    return True


def isPrimeProofsqubeOdd(p, q):
    n = p ** 2 * q ** 3
    if "200" not in str(n):
        return False
    for digit in range(len(str(n))):
        for i in range(0, 10):
            m = str(n)[:digit] + str(i) + str(n)[digit + 1:]
            if isPrime(int(m)):
                return False
    return True


def problem200():
    primes = primesUpTo(169249+2)
    candidates = []
    # Do not know why I can make this assumption
    # There are other types of primeproof sqube but they 
    # are all much larger
    for p in [2,5]:
        for q in primes:
            if q == 2 or q == 5: continue
            candidates.append((p, q))
            candidates.append((q, p))
    candidates.sort(key=lambda x: x[0]**2 * x[1]**3)
    found = 1
    seen = {200}
    for p, q in candidates:
        if 2 in (p, q) or 5 in (p, q):
            if isPrimeProofsqubeEven(p, q):
                found += 1
        else:
            if isPrimeProofsqubeOdd(p, q):
                found += 1
        if found == 200:
            return p ** 2 * q ** 3
    return seen

from cProfile import run
if __name__ == "__main__":
    run("problem200()")
    print(problem200() == 229161792008)