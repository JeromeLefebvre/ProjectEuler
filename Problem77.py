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

def numberOfWays(n,checker,max):
	count = 0
	if n <= 3:
		return 0
	primeList = checker[0:max]
	primeList.reverse()
	for p in primeList:
		if checker.isPrime(n-p) and n-p <= p:
			count += 1
		count += numberOfWays(n-p,checker,p)
	return count

def problem77():
	checker = primes(save=True,initial=False)
	record = 0
	for i in range(1,100):
		r = numberOfWays(i,checker,i)
		if r >= 5000:
			return(i)

from PE_primes import isPrime
from itertools import dropwhile
def problem77():
	from PE_primes import primesUpTo
	primeList = list(primesUpTo(30000))
	record = 0
	def numberOfWaysa(n,maximum,_d={(3,3):1,(3,2):0,(2,2):1}):
		if (n,maximum) in _d:
			return _d[(n,maximum)]
		count = 0
		if isPrime(n) and isPrime(maximum):
			count += 1
		for p in dropwhile(lambda x: x>=maximum or n-x <=0, primeList[::-1]):
			#if n -p <= 0: continue
			#if isPrime(n-p) and n-p <= p:
			#	print(n,p)
			#	count += 1
			count += numberOfWaysa(n-p,p)
		_d[(n,maximum)] = count
		return count
	print("**",numberOfWaysa(71,71))
	
	for i in range(1,100):
		r = numberOfWaysa(i,i)
		if r >= 110:
			return i
	
from cProfile import run
if __name__ == "__main__":
	run("problem77()")
	print(problem77())
 