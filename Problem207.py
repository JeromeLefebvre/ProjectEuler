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

from quadratics import solveIntegerQuadratic

def positiveSolution(a, b, c):
    return [s for s in solveIntegerQuadratic(a, b, c) if s > 0]

def isPowerOf2(x):
    '''Returns if x is a power of 2'''
     # easy check since a power of 2 looks like 100000 in binary and 2**n -1 looks like 01111111
    return x != 0 and ((x & (x - 1)) == 0)

def P(frac):
    perfect = 0
    notperfect = 0
    for l in count(1):
        k = l*(l+1)    
        try:
            x = positiveSolution(1, -1, -k)[0]
            if isPowerOf2(x):
                perfect += 1
            else:
                notperfect += 1
        except:
            pass
        if perfect / (perfect + notperfect) < frac:
            return k

def problem207():
    return P(1 / 12345)

from cProfile import run
if __name__ == "__main__":
    run("problem207()")
    print(problem207() == 44043947822)
