#!/usr/local/bin/python3.3

'''
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
'''

'''
Notes on problem 70():
'''


def isPermutation(a,b):
	a = str(a)
	b = str(b)
	if set(a) != set(b):
		return False
	for p in set(a):
		if a.count(p) != b.count(p):
			return False
	return True

'''
Noticed that all records where the products of two primes, so ran over all candidates
'''
def problem70a():
	checker = primes(save=True,initial=True)
	record = 1000000000
	for n in range(1,10**6):
		ph = checker.phi(n)
		if isPermutation(n,ph) and n/ph < record:
			print(n,checker.factors(n))
			record = n/ph

from itertools import combinations
def problem70b():
	checker = primes(save=True,initial=True)
	record = 1000000000
	for p in checker[2:10**6]:
		for q in checker[2:10**7//p]:
			n = p*q
			ph = (p-1)*(q-1)
			if isPermutation(n,ph) and n/ph < record:
				print(n)
				record = n/ph


def problem70():
	from PE_primes import primesUpTo
	GOAL = 10**7
	primes = primesUpTo(2*int(GOAL**(1/2)))
	record = 1000000000
	for index, p in enumerate(primes[1:]):
		for q in primes[index:]:
			if q > GOAL//p: break
			n = p*q
			ph = (p-1)*(q-1)
			if isPermutation(n,ph) and n/ph < record:
				record = n/ph
				recordN = n
	return recordN

from cProfile import run
if __name__ == "__main__":
	print(problem70() == 8319823)
	run("problem70()")
 