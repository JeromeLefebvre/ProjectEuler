
'''


primes = [2,3,5]

pickle.dump( primes, open( "primes.dump", "wb" ) )

primesload = pickle.load( open( "primes.dump", "rb" ) )

print(primesload)
'''

def iPrimes():
	''' Generate an infinite sequence of prime numbers.
		Taken from: http://stackoverflow.com/questions/567222/simple-prime-generator-in-python
	'''
	D = {}   
	q = 2
	while True:
		if q not in D:
			yield q        
			D[q * q] = [q]
		else:
			for p in D[q]:
				D.setdefault(p + q, []).append(p)
			del D[q]
		q += 1

import pickle
from itertools import combinations
from projectEuler import product

class primes():
	'''A class that checks if a number is prime'''
	def __init__(self,save=True,initial=False):
		self._primeData = "primes.dump"
		self._primeSieveData = "primesSieve.dump"
		if not initial:
			try:
				with open(self._primeData):
					self.knowPrimes = pickle.load(open(self._primeData, "rb"))
					self.currentNumber = self.knowPrimes[-1]+1
			except IOError:
				self.knowPrimes = [2]
				pickle.dump(self.knowPrimes, open(self._primeData, "wb"))
				self.currentNumber = 3
			try:
				with open(self._primeSieveData):
					self.primeSieve = pickle.load(open(self._primeSieveData, "rb"))
			except IOError:
	   			self.primeSieve = {4:[2]}
	   			pickle.dump(self.primeSieve, open(self._primeSieveData, "wb"))
	   	else:
	   		self.currentNumber = 3
	   		self.primeSieve = {4:[2]}
	   		self.knowPrimes = [2]
		self.save = save
		


	def __del__(self):
		# Need picke to be imported here so that we can use the pickle module safely when storing the old data
		import pickle
		if self.save:
			pickle.dump(self.knowPrimes, open(self._primeData, "wb"))			
			pickle.dump(self.primeSieve, open(self._primeSieveData, "wb"))


	def cleanup(self):
		'''Deletes the associated file, should be called with save=False'''
		import os
		os.remove(self._primeData)
		os.remove(self._primeSieveData)
		self.currentNumber = 2
		self.knowPrimes = []
		self.primeSieve = {}

	def addPrimeUpTo(self,q):
		'''Adds all primes up to a certain bound'''
		while self.currentNumber <= q:
			self.addPrime()

	def addPrime(self):
		'''adds the next prime'''
		addedNew = False
		while not addedNew:
			if not self.currentNumber in self.primeSieve:
				self.knowPrimes.append(self.currentNumber)
				self.primeSieve[self.currentNumber**2] = [self.currentNumber]
				addedNew = True
			else:
				for p in self.primeSieve[self.currentNumber]:
					self.primeSieve.setdefault(p + self.currentNumber, []).append(p)
				del self.primeSieve[self.currentNumber]
			self.currentNumber += 1


	def isPrime(self,q):
		'''Checks if a certain number is prime'''
		self.addPrimeUpTo(q)
		return q in self.knowPrimes
		
	def factors(self,q):
		'''Returns a list of all the prime factors, with multiplicity'''
		if q == 1 or q in self.knowPrimes:
			return [q]
		factors = []
		for p in self.knowPrimes:
			while q % p == 0:
				factors.append(p)
				q = q//p
			if q == 1:
				return factors
			if q > self.knowPrimes[-1]:
				self.addPrime()

	def divisors(self,q):
		factors = self.factors(q)
		divisors = [1]
		for numDiv in range(1,len(factors)+1):
			for c in combinations(factors, numDiv):
				divisors.append(product(c))
		return set(divisors)

	def rwh_primes2(self,n):
	    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
	    """ Input n>=6, Returns a list of primes, 2 <= p < n """
	    correction = (n%6>1)
	    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
	    sieve = [True] * (n//3)
	    sieve[0] = False
	    for i in range(int(n**0.5)//3+1):
	      if sieve[i]:
	        k=3*i+1|1
	        sieve[      ((k*k)//3)      ::2*k]=[False]*((n//6-(k*k)//6-1)//k+1)
	        sieve[(k*k+4*k-2*k*(i&1))//3::2*k]=[False]*((n//6-(k*k+4*k-2*k*(i&1))//6-1)//k+1)
	    self.knowPrimes = [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]


c = primes(save=True, initial=False)
print(c.divisors(12))
