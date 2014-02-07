#!/usr/local/bin/python3.3

'''
Problem 71
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.
'''

'''
Notes on problem 71():
Using Fractions seems temping, but much too slow
'''
from projectEuler import gcd
from fractions import Fraction

def problem71a():
    seen = []
    record = 1/8
    bestD = 8
    bestN = 1
    for d in range(1,10**6+1):
        for n in range(int(bestN*(d+1)/d),int(3*d/7)):
            if 7*n < 3*d:
                if n/d > record:
                    record = n/d
                    bestD = d
                    bestN = n
            else:
                break
    return bestN

def problem71():
    d = 10**6
    return (3*d)//7 - 1

from cProfile import run
if __name__ == "__main__":
    run("problem71()")
    print(problem71() == 428570)
