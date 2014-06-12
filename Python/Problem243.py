

'''
Problem 243

A positive fraction whose numerator is less than its denominator is called a proper fraction.
For any denominator, d, there will be d−1 proper fractions; for example, with d = 12:
1/12 , 2/12 , 3/12 , 4/12 , 5/12 , 6/12 , 7/12 , 8/12 , 9/12 , 10/12 , 11/12 .

We shall call a fraction that cannot be cancelled down a resilient fraction.
Furthermore we shall define the resilience of a denominator, R(d), to be the ratio of its proper fractions that are resilient; for example, R(12) = 4/11 .
In fact, d = 12 is the smallest denominator having a resilience R(d) < 4/10 .

Find the smallest denominator d, having a resilience R(d) < 15499/94744 .

'''

from projectEuler import primes,phiFromFactors, generateFactors,product

from itertools import combinations

import random
from math import log
def maxExponent(p,maximum):
	if maximum <= 1: return 0
	return int(log(maximum)/log(p))

def phiFromFactors(factors):
	if factors == []: return 0
	ph = 1
	for p in set(factors):
		ph *= p**factors.count(p) - p**(factors.count(p) - 1)
	return ph

def genFactors(l = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], maximum=10**10):
	exp = {}
	n = maximum
	# 1 until
	q = random.choice(l)
	one = 1
	for p in l:
		try: 
			exp[p] = random.randint(one,maxExponent(p,n))
		except:
			exp[p] = 0
		n //= p**exp[p]
		if p == q:
			one = 0
	phi = product([p**exp[p] - p**(exp[p] - 1) for p in l if exp[p] > 0])
	return phi, product([p**exp[p] for p in l])

genFactors(maximum=1000)

#892371480
#200560490130
#70274254050
# 10000 -> 36427776000
def problem243():
	record = 2*3*5*7*11*13*17*19*23*29*31
	record = 70274254050
	for i in range(1,10000):
		phi, n = genFactors(maximum=record)
		r = phi/(n-1)
		if r < 15499/94744 and n < record:
			record = n
	return record
			
	

if __name__ == "__main__":
	print(problem243())




68916891abcABC