#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=293
Pseudo-Fortunate Numbers
Problem 293
'''

'''
Notes on problem 293():
'''

from PE_primes import iPrime, isPrime, primesUpTo, factorize
from itertools import accumulate,count

def generateAdmissible(n,primes,start=1,factors=()):
	'''This generates all admissible numbers between 2 and n'''
	if start <= n:
		for a in primes[start:n]:
			yield factors + (a,)
			for c in generateFactors(n//a,primes,a,factors+(a,)):
				yield c

def generateAdmissible(n,primes,start=2,primeIndex=0):
	if start <= n:
		yield start
		for c in generateAdmissible(n,primes,start*primes[primeIndex],primeIndex): yield c
		for c in generateAdmissible(n,primes,start*primes[primeIndex+1],primeIndex+1): yield c


def problem293():
	GOAL = 10**3
	primes = []
	maximum = 1
	for p in iPrime():
		maximum *= p
		primes.append(p)
		if maximum > GOAL: break
	print(primes)
	admissible = []
	for c in generateAdmissible(GOAL,primes):
		admissible.append(c)
	print(sorted(admissible))

def problem293():
	GOAL = 10**9
	primes = []
	maximum = 1
	for p in iPrime():
		maximum *= p
		primes.append(p) # need one more beyond what is required
		if maximum > GOAL: break
	admissible = []
	total = 0
	num = 0
	for c in generateAdmissible(GOAL,primes):
		#print(c, sorted(factorize(c)))
		if c > GOAL: continue
		num += 1
		for d in count(3,2):
			if isPrime(c+d):
				total += d
				break
	return num, total

from cProfile import run
if __name__ == "__main__":
	#run("problem293()")
	print(problem293()) 