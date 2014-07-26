#!/usr/local/bin/python3.3

'''
Problem 27
Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
'''

from itertools import product

from pe.orderedList import Orderedlist
from pe.primes import isPrime, primesUpTo


def problem27():
    record = 0
    ab = 0
    checker = Orderedlist(primesUpTo(1998))
    # We know there is a record of 80
    # this removes many possibilities for low values of b
    # since the most number of primes for f(n) is b-1
    for b in checker[80:1000]:
        for p1 in checker[0:1000 + b + 1]:
            a = p1 - b - 1
            n = 2
            p2 = a + p1 + (2 * n - 1)
            while isPrime(abs(p2)):
                n += 1
                p2 = a + p2 + (2 * n - 1)
            if n > record:
                record = n
                ab = a * b
    return ab

if __name__ == "__main__":
    print(problem27() == -59231)
    from cProfile import run
    run("problem27()")