#!/usr/local/bin/python

'''
http://projecteuler.net/problem=207
Integer partition equations
Problem 207
'''

'''
Notes on problem 207():
'''

from itertools import count
from math import log

from quadratics import solveIntegerQuadratic

PRECISION = 10


def positiveSolution(a, b, c):
    return [s for s in solveIntegerQuadratic(a, b, c) if s > 0]

from decimal import *
getcontext().prec = PRECISION


def f(k):
    radical = Decimal(1) + Decimal(4) * k
    radical = Decimal(1) + radical.sqrt()
    radical /= Decimal(2)
    return radical.ln() / Decimal(2).ln()


def isInteger(a):
    return int(a) == a.quantize(Decimal('0.0000001'))


def P(n):
    perfect = 0
    notperfect = 0
    k = Decimal(1)
    while True:
        t = f(k)
        if isInteger(2 ** t):
            if isInteger(t):
                perfect += 1
            else:
                notperfect += 1
        if k >= n:
            return perfect, (perfect + notperfect)
        k += 1


def ispowerOf2(x):
    return x in {2 ** n for n in range(1, 100)}


def P(frac):
    perfect = 0
    notperfect = 0
    l = 1
    while True:
        k = l*(l+1)    
        try:
            x = positiveSolution(1, -1, -k)[0]
            if ispowerOf2(x):
                perfect += 1
            else:
                notperfect += 1
        except:
            pass
        if perfect / (perfect + notperfect) < frac:
            return k
        l += 1

# 44043947822
def problem207():
    return P(1 / 12345)

'''
Split P(n) so that it calls a function to check if perfect or not
make it return -1 for notperfect, 1 for perfect 0 for nothing

Make a list of values you know are perfect, not perfect, nothing and use tests to check how things changes
'''
from cProfile import run
if __name__ == "__main__":
    run("problem207()")
    print(problem207() == 44043947822)
