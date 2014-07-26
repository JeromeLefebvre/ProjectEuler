#!/usr/local/bin/python3.3

'''
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

n	Relatively Prime	φ(n)	n/φ(n)
2	1	1	2
3	1,2	2	1.5
4	1,3	2	2
5	1,2,3,4	4	1.25
6	1,5	2	3
7	1,2,3,4,5,6	6	1.1666...
8	1,3,5,7	4	2
9	1,2,4,5,7,8	6	1.5
10	1,3,7,9	4	2.5
It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
'''

'''
Notes on problem 69():
This can easily be improved, as the max phi is simply a product of primes
'''
from pe.basic import product
from pe.factors import genProducts


def phiFromFactors(factors):
    if factors == []:
        return 0
    ph = 1
    for p in set(factors):
        ph *= p ** factors.count(p) - p ** (factors.count(p) - 1)
    return ph


def problem69():
    record = 0
    for n in genProducts(10 ** 6, [2, 5, 7, 3, 11, 13, 17, 19, 21]):
        if product(n) == 1:
            continue
        phi = product(n) / phiFromFactors(n)
        if phi > record:
            record = phi
            recordN = n
    return product(recordN)

if __name__ == "__main__":
    print(problem69() == 510510)
    from cProfile import run
    run("problem69()")
