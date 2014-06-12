#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=179()
Consecutive positive divisors
Problem 179
Find the number of integers 1 < n < 107, for which n and n + 1 have the same number of positive divisors. For example, 14 has the positive divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.
'''

'''
Notes on problem 179():
'''
from projectEuler import rwh_primes2,product,sigmaFromFactors,primes,generateFactors
from MillerRabin import isPrime

def factors(n, primes):# , _d={1:[1],2:[2]}):
	m = n
	factor = []
	for p in primes:
		while n % p == 0:
			factor.append(p)
			n //= p
		if n == 1:
			return factor
	# it is prime
	return [n]

def sigma(n,primes):
	l = factors(n,primes)
	return product([l.count(p) + 1 for p in set(l)])

def problem179a():
	GOAL = 10**5
	#checker = primes(save=True,initial=False)
	primes = rwh_primes2(GOAL//2)
	previous = 0
	# counting 2
	count = 1
	for n in range(3,GOAL):
		# If it n+1 is prime, we can skip this number
		if isPrime(n):
			sig = 2
		else:
			sig = sigma(n,primes)
		if sig == previous:
			count += 1
		previous = sig
	return count


def problem179():
	GOAL = 10**7
	checker = primes(save=True,initial=False)
	#primes = rwh_primes2(GOAL//2)
	previous = 0
	# counting 2
	count = 0
	d = {1:1}
	for n in generateFactors(GOAL+1, checker):
		d[product(n)] = sigmaFromFactors(n)
	for n in range(1,GOAL):
		if d[n] == d[n+1]: count+=1
	return count


if __name__ == "__main__":
	print(problem179())
 