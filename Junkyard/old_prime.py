'''
class isPrime():
	'''A class that checks if a number is prime'''
	def __init__(self):
		self.listOfPrimes = []
		self.primeSource = iPrimes()
		# take out 2 from the list
		for a in self.primeSource:
			self.listOfPrimes.append(a)
			break

	def addPrimes(self,q):
		# add all the primes to the square of the number
		# this is enough to factorize it
		if q > (self.listOfPrimes[-1])**2:
			for a in self.primeSource:
				if a not in self.listOfPrimes:
					self.listOfPrimes.append(a)
				if a**2 > q:
					break

	def addPrime(self):
		'''adds the next prime'''
		for a in self.primeSource:
			if a not in self.listOfPrimes:
				self.listOfPrimes.append(a)
				break

	def check(self,q):
		if q <= self.listOfPrimes[-1]:
			return q in self.listOfPrimes
		self.addPrimes(q)
		for p in self.listOfPrimes:
			if q % p == 0:
				return False
		return True
		
	def factorize(self,q):
		if q == 1 or q in self.listOfPrimes:
			return [q]
		factors = []
		for p in self.listOfPrimes:
			while q % p == 0:
				factors.append(p)
				q = q//p
			if self.check(q):
				return factors + [q]
			if p == self.listOfPrimes[-2] or q > self.listOfPrimes[-1]:
				self.addPrime()
		# if we couldn't find any factors, the number must have been prime
		if factors == []:
			return [q]
		return factors

	def divisors(self,q):
		factors = self.factorize(q)
		divisors = [1]
		for numDiv in range(1,len(factors)+1):
			for c in itertools.combinations(factors, numDiv):
				divisors.append(product(c))
		return set(divisors)
'''
