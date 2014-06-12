#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=88()
Product-sum numbers
Problem 88
A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers, {a1, a2, ... , ak} is called a product-sum number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.

For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.

For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number. The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.

k=2: 4 = 2 × 2 = 2 + 2
k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; note that 8 is only counted once in the sum.

In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is {4, 6, 8, 12, 15, 16}, the sum is 61.

What is the sum of all the minimal product-sum numbers for 2≤k≤12000?
'''

'''
Notes on problem 88():
'''
from factorGenerating import genFactors

from PE_basic import product

def problem88():
    d = {k:10**8 for k in range(1,12000+1)}
    def candidates(a, l, p, s):
        m = len(l)
        if a == 1: maximum = a
        else: maximum = a+1
        for b in range(1,maximum):
            newL = l + [b]
            k = m+1 + p*b - (s+b)
            if k > 12000: return
            d[k] = min(d[k], p*b)
            candidates(b,newL,p*b, s+b)
    for a in range(2,1453):
        candidates(a,[a],a, a)
    return sum({d[k] for k in d if k>1})

from cProfile import run
if __name__ == "__main__":
    run("problem88()")
    print(problem88() == 7587457)
 