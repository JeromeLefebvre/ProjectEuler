
class orderedlist:
	def __init__(self,_ordered = []):
		self.ordered = _ordered
	
	def indexAbove(self,q):
		'''Returns the index of the largest or equal element above
		in hopefully log(n) time, n = len(self.ordered)'''
		# There is no elements greater than q in the list
		# returns an error. Maybe the better choice is to return an -1
		if q > self.ordered[-1]:
			raise IndexError
		# If it is lower than the entire list, return 0 (the rest of the algorithm breaks in any case)
		if q < self.ordered[0]: return 0
		# we now try to narrow down 
		low, high = 0, len(self.ordered) - 1
		guess = low + (high - low)//2
		while True:
			
			if self.ordered[guess] > q:
				high = guess
			else:
				low = guess
			# we now narrowed it enough that we only need to check one last element
			if (high - low) <= 1:
				if self.ordered[low] == q: return low
				else: return high
			guess = low + (high - low)//2

	def indexBelow(self,q):
		'''Returns the index of the largest or equal element above
		in hopefully log(n) time, n = len(self.ordered)'''
		# There is no elements greater than q in the list
		# returns an error. Maybe the better choice is to return an -1
		if q < self.ordered[0]:
			raise IndexError
		# If it is lower than the entire list, return 0 (the rest of the algorithm breaks in any case)
		if q > self.ordered[-1]: return -1
		# we now try to narrow down 
		low, high = 0, len(self.ordered) - 1
		while True:
			guess = low + (high - low)//2	
			if self.ordered[guess] < q:
				low = guess
			else:
				high = guess
			# we now narrowed it enough that we only need to check one last element
			if (high - low) <= 1:
				if self.ordered[high] == q: return high
				else: return low

	def __getitem__(self,pos):
		start, stop = pos.start,pos.stop
		return self.ordered[self.indexAbove(start):self.indexBelow(stop)+1]
	
	def __str__(self):
		return str(self.ordered)

from projectEuler import rwh_primes2, product

def genFactors(n):
	# The funny + 20 is that I need to check not just primes up to n but the prime after that as well
	return generateFactors(n, orderedlist(rwh_primes2(n+30)),genOne=True)

def generateFactors(n,checker,start=1,factors=[], genOne=False):
	'''This generates all numbers between from 2 up to n as their list of factors'''
	if genOne:
		yield [1]
	if start <= n//product(factors):
		for a in checker[start:n//product(factors)]:
			yield factors + [a]
			for c in generateFactors(n,checker,a,factors+[a]):
				yield c

def genFactorsA(n):
	# The funny + 20 is that I need to check not just primes up to n but the prime after that as well
	return generateFactorsA(n, orderedlist(rwh_primes2(n+30)),genOne=True)

def generateFactorsA(n,checker,start=1,factors=[], genOne=False):
	'''This generates all numbers between from 2 up to n as their list of factors'''
	if genOne:
		yield [1]
	if start <= n//product(factors):
		# The -1 is to make sure 2 is included when we are at 3
		alef = checker.indexAbove(start)
		tav = checker.indexBelow(n//product(factors))+1
		for i in range(alef,tav):
			a = checker.ordered[i]
			yield factors + [a]
			for c in generateFactorsA(n,checker,a,factors+[a]):
				yield c

count = 0
for a in genFactorsA(10**7):
	count += 1
print(count)
'''
m = [-1,2,3,4,10,33,141]
l = orderedlist(m)
print(m[l.indexBelow(2)] == 2)
print(m[l.indexBelow(15)] == 10)
print(m[l.indexBelow(3)] == 3)
print(m[l.indexBelow(3)])
print(m[l.indexBelow(2200)] == 141)
print(m[l.indexAbove(4)] == 4)
print(m[l.indexAbove(10)] == 10)
print(m[l.indexAbove(1)] == 2)
print(m[l.indexAbove(5)] == 10)
print(m[l.indexAbove(4)] == 4)
print(m[l.indexAbove(2)] == 2)
print(m[l.indexAbove(140)] == 141)
print(m[l.indexAbove(0)] == 2)
print(m[l.indexAbove(-5)] == -1)
print(m[l.indexAbove(3)] == 3)
print("Testing intervals")
print(l[3:4] == [3,4])
print(l[5:10] == [10])
print(l[5:11] == [10])
print(l[4:11] == [4,10])
print(l[1:11] == [2,3,4,10])
'''