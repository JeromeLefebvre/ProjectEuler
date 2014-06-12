#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=249
Prime Subset Sums
Problem 249
'''

'''
Notes on problem 249():
'''

from PE_primes import primesUpTo, isPrime
from PE_basic import powerset
from collections import defaultdict
from itertools import accumulate

def runningTotal(iterable):
    total = 0
    for a in iterable:
        total += a
        yield a,total

def problem249(): 
    primes = primesUpTo(5000)
    sums = defaultdict(int)
    sums[0] = 1
    for p,total in runningTotal(primes):
        for j in range(total,p-1,-1):
            sums[j] = sums[j] + sums[j-p]
    return sum([sums[k] for k in range(total+1) if isPrime(k)]) % 10**16

from cProfile import run
if __name__ == "__main__":
    run("problem249()")
    print(problem249() == 9275262564250418) 