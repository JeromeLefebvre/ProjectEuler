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
'''
from projectEuler import primes, gcd, radFromFactors, product, generateFactors, iPrimes

def relPrimeFromFactors(e,f):
	return not any( p in f for p in set(e))

def relPrimeFirstFactors(e,n):
	if e == [1]:
		return True
	return not any( n % p == 0 for p in set(e))

def radA(n, _d={1:1,2:2,3:3,4:2,5:5}):
	if n not in _d:
		_d[n] = radFromFactors(factor(n))
	return _d[n]

def factor(n, _memo={1: []}):
    """returns a list of the prime factors of integer n"""
    if n <= 0: raise ValueError("Can't factor %r" % n)
    localmemo = {}
    orgn = n
    p = iPrimes()  # yields an infinite iterable
    for x in p:
        if n in _memo:
            for k in localmemo:
                localmemo[k].extend(_memo[n])
            _memo.update(localmemo)
            return _memo[orgn]
        localmemo[n] = []
        while n % x == 0:
            n = n//x
            for k in localmemo:
                localmemo[k].append(x)
        if n == 0:
        	return 1


def problem127():
	checker = primes(save=True,initial=False)
	GOAL = 120000  # 60
	total = 0
	count = 0
	#global knowPrimes
	#knowPrimes = rwh_primes2(GOAL//2 + 1)
	#for d in generateFactors(GOAL, checker):
	for prod in generateFactors(GOAL,checker):
		c = product(prod)
		radc = product(set(prod))
		for a in [n for n in range(1,c//2) if not any( n % p == 0 for p in set(prod))]:

			#for e in generateFactors(c//2, checker,genOne=True):
			#a = product(e)
			# we now have b > a, a + b = c
			b = c - a
			#print(a,b,c)
			#f all([relPrimeFromFactors(d,e), relPrimeFirstFactors(e,b), relPrimeFirstFactors(d,b)]) and radFromFactors(e)*checker.rad(b)*radFromFactors(d) < c:
			#if all([relPrimeFromFactors(d,e), gcd(a,b), relPrimeFirstFactors(d,b)]) and radFromFactors(e)*checker.rad(b)*radFromFactors(d) < c:
			radb = radA(b)
			if radb < c/radc and radb*radA(a)*radc < c:
				total += c
				count += 1
	return total, count


if __name__ == "__main__":
	print(problem127())
 