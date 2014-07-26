#!/usr/local/bin/python3.3

'''
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
'''

'''
Notes on problem 70():
'''

from itertools import combinations

from pe.primes import primesUpTo
from pe.digits import isPermutation

'''
Noticed that all records where the products of two primes, so ran over all candidates
'''
def problem70():
    GOAL = 10 ** 7
    primes = primesUpTo(2 * int(GOAL ** (1 / 2)))
    record = 1000000000
    for index, p in enumerate(primes[1:]):
        for q in primes[index:]:
            if q > GOAL // p:
                break
            n = p * q
            ph = (p - 1) * (q - 1)
            if isPermutation(n, ph) and n / ph < record:
                record = n / ph
                recordN = n
    return recordN

if __name__ == "__main__":
    print(problem70() == 8319823)
    from cProfile import run
    run("problem70()")
