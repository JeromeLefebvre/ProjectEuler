#!/usr/local/bin/python3.3

'''
It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?
'''

'''
Notes on problem 77():
'''
#from projectEuler import primes

from PE_primes import primesUpTo
from itertools import count

def problem77():
    primes = primesUpTo(100)
    for target in count(11):
        ways = [1] + [0] * target
        for prime in primes:
            for j in range(prime, target + 1):
                ways[j] += ways[j - prime]
        if ways[target] > 5000:
            return target

from cProfile import run
if __name__ == "__main__":
    run("problem77()")
    print(problem77() == 71)
