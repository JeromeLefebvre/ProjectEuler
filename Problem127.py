#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=127()
abc-hits
Problem 127
The radical of n, rad(n), is the product of distinct prime factors of n. For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.

We shall define the triplet of positive integers (a, b, c) to be an abc-hit if:

GCD(a, b) = GCD(a, c) = GCD(b, c) = 1
a < b
a + b = c
rad(abc) < c
For example, (5, 27, 32) is an abc-hit, because:

GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 1
5 < 27
5 + 27 = 32
rad(4320) = 30 < 32
It turns out that abc-hits are quite rare and there are only thirty-one abc-hits for c < 1000, with ∑c = 12523.

Find ∑c for c < 120000.
'''

'''
Notes on problem 127():
Very slow
'''

from PE_factors import genFactors
from PE_basic import product

def problem127():
    GOAL = 120000

    rad = {}  # rad[6] = {2,3}, radn[8] = {2}
    for primes in genFactors(GOAL):
        rad[product(primes)] = (set(primes), product(set(primes)))

    def relprime(s, t):
        return s & t == set()

    found = 0
    total = 0
    for b in range(1, GOAL):
        for a in range(1, min(b, GOAL - b)):
            c = a + b
            x, y, z = rad[a], rad[b], rad[c]
            if x[0] & y[0] != set():
                continue
            if x[1] * y[1] * z[1] < c:
                found += 1
                total += c
    return total


if __name__ == "__main__":
    print(problem127() == 18407904)
