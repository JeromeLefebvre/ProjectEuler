
import pickle
from itertools import combinations
class primes():
	'''A class that checks if a number is prime'''
	def __init__(self,save=True,initial=False):
		self.save = save
		self._primeData = "primes.dump"
		self._primeSieveData = "primesSieve.dump"
		self._primesUpToData = "primesUpTo.dump"
		self._factorData = "factors.dump"
		self._currentNumber = "currentNumber.dump"
		self._DefaultData = {"knowPrimes":[2],"currentNumber":3,"primesUpTo":{1:0,2:1},"primeSieve" :{4:[2]},"knowFactors":{1:[1],2:[2]} }
		if not initial:
			import os
			if os.path.isfile(self._primeData):
				with open(self._primeData,"rb") as data:
					self.knowPrimes = pickle.load(data)
			else:
				self.knowPrimes = self._DefaultData["knowPrimes"]
			if os.path.isfile(self._primeSieveData):
				with open(self._primeSieveData,"rb") as data:
					try:
						self.primeSieve = pickle.load(data)
					except EOFError:
						# Every once in a while, the file seems to get corrupted
						self.primeSieve =  self._DefaultData["primeSieve"]
			else:
	   			self.primeSieve = self._DefaultData["primeSieve"]
			if os.path.isfile(self._primesUpToData):
				with open(self._primesUpToData,"rb") as data:
					self.primesUpTo = pickle.load(data)
			else:
	   			self.primesUpTo = self._DefaultData["primesUpTo"]
			if os.path.isfile(self._factorData):
				with open(self._factorData,"rb") as data:
					self.knowFactors = pickle.load(data)
			else:
				self.knowFactors = self._DefaultData["knowFactors"]
			if os.path.isfile(self._currentNumber):
				with open(self._currentNumber,"rb") as data:
					self.currentNumber = pickle.load(data)
			else:
				self.currentNumber = self._DefaultData["currentNumber"]
		else:
	   		self.setDefault()
		
		
	def setDefault(self):
		self.currentNumber = self._DefaultData["currentNumber"]
		self.primeSieve =  self._DefaultData["primeSieve"]
		self.knowPrimes =  self._DefaultData["knowPrimes"]
		self.primesUpTo = self._DefaultData["primesUpTo"]
		self.knowFactors = self._DefaultData["knowFactors"]

	def __del__(self):
		# Need picke to be imported here so that we can use the pickle module safely when storing the old data
		import pickle
		if self.save:
			pickle.dump(self.knowPrimes, open(self._primeData, "wb"))
			pickle.dump(self.primeSieve, open(self._primeSieveData, "wb"))
			pickle.dump(self.primesUpTo, open(self._primesUpToData, "wb"))
			pickle.dump(self.knowFactors, open(self._factorData, "wb"))
			pickle.dump(self.currentNumber, open(self._currentNumber, "wb"))


	def cleanup(self):
		'''Deletes the associated file'''
		import os
		if os.path.isfile(self._primeData):
			os.remove(self._primeData)
		if os.path.isfile(self._primeSieveData):
			os.remove(self._primeSieveData)
		if os.path.isfile(self._primesUpToData):
			os.remove(self._primesUpToData)
		if os.path.isfile(self._factorData):
			os.remove(self._factorData)
		if os.path.isfile(self._currentNumber):
			os.remove(self._currentNumber)			
		self.setDefault()

	def addPrimeUpTo(self,q):
		'''Adds all primes up to a certain bound'''
		while self.currentNumber <= q:
			self.addPrime(stopAt=q)

	def addPrime(self,stopAt=False):
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
			if stopAt and stopAt <= self.currentNumber:
				break

	def sigma(self,q):
		l = self.factors(q)
		return product([l.count(p) + 1 for p in set(l)])

	def isPrime(self,q):
		'''Checks if a certain number is prime'''
		self.addPrimeUpTo(q)
		return q in self.knowPrimes
		
	def factors(self,q):
		'''Returns a list of all the prime factors, with multiplicity'''
		savedInput = q
		self.addPrimeUpTo(q**(1//2))
		if q in self.knowFactors:
			return self.knowFactors[q]
		if q in self.knowPrimes:
			self.knowFactors[savedInput] = [savedInput]
			return [q]
		factors = []
		for p in self.knowPrimes:
			while q % p == 0:
				factors.append(p)
				q = q//p
			if q == 1:
				self.knowFactors[savedInput] = factors
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

	def rad(self,n):
		return product(set(self.factors(n)))
	
	def nth(self,n):
		''' returns the nth prime '''
		# We must first add all the primes up to there
		while len(self.knowPrimes) <= n-1:
			self.addPrime()
		return self.knowPrimes[n-1]

	def indexOfFirstPrimeBelow(self,n):
		'''returns the index of largest prime below or equal to n'''
		''' This algorithm does not work well'''
		'''Note that this is not defined for 0 and 1, it will return -1'''
		self.addPrimeUpTo(n)
		for index, p in enumerate(self.knowPrimes):
			if p > n:
				return index - 1
			if p == n:
				return index
		return index 

	def __getitem__(self, arg):
		'''Should return all primes between the two values'''
		starting = arg.start
		if arg.start == 0 or arg.start == 1:
			starting = 0
		else:
			starting = self.indexOfFirstPrimeBelow(starting) + 1
		self.addPrimeUpTo(arg.stop)
		return self.knowPrimes[starting:self.indexOfFirstPrimeBelow(arg.stop)+1]

	def pi(self,n):
		'''returns the number of primes below or equal to n'''
		self.addPrimeUpTo(n)
		if not n in self.primesUpTo:
			self.primesUpTo[n] = self.indexOfFirstPrimeBelow(n) + 1
		return self.primesUpTo[n]

	def phi(self,n):
		if n == 0: return 0
		f = self.factors(n)
		ph = 1
		for p in set(f):
			ph *= p**f.count(p) - p**(f.count(p) - 1)
		return ph