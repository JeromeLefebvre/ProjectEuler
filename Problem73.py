#!/usr/local/bin/python3.3

'''
Problem 73
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?
'''

'''
Notes on problem 73():
'''

from fractions import gcd
from PE_basic import product
def relPrimeFromFactors(n,d):
	for p in set(n):
		if p in d:
			return False
	return True

def generateFactors(n,start,checker, factors=[]):
	if start <= n//product(factors):	 
		for a in checker[start:n//product(factors)]:
			yield factors + [a]
			for c in generateFactors(n,a,checker,factors+[a]):
				yield c

def problem73a():
	total = 0
	from factorGenerating import genFactors
	for d in genFactors(12000):
		if d in [(1,)]: continue
		for n in genFactors(product(d)):
			r = product(n)/product(d)
			if relPrimeFromFactors(n,d) == 1 and r > 1/3 and r < 1/2:
				total += 1
	return total

def problem73():
	total = 0
	for d in range(1,12000+1):
		for n in range(d//3-1,d//2+1):
			if gcd(d,n) == 1 and n/d < 1/2 and n/d > 1/3:
				total += 1
	return total

from cProfile import run
if __name__ == "__main__":
	print(problem73() == 7295372)
	run("problem73()")