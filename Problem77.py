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

def numberOfWaysa(n,primeList,maximum):
	from PE_primes import isPrime
	from itertools import dropwhile
	count = 0
	if n <= 3:
		return 0
	#primeList = checker[0:max]
	#primeList.reverse()
	for p in dropwhile(lambda x: x>=maximum, primeList[::-1]):
		if n -p <= 0: continue
		if isPrime(n-p) and n-p <= p:
			count += 1
		count += numberOfWaysa(n-p,primeList,p)
	return count

def problem77a():
	from PE_primes import primesUpTo
	primeList = list(primesUpTo(30000))
	record = 0
	for i in range(1,100):
		r = numberOfWaysa(i,primeList,i)
		if r >= 5000:
			return(i)

if __name__ == "__main__":
	print(problem77a())
 