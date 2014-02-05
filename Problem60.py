
'''
Problem 60

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
'''

from itertools import combinations
from functools import reduce

from PE_primes import isPrime, primesUpTo,iPrime
from PE_digits import numberOfDigits
def remarkable(p,q):
	return isPrime(int(str(p) + str(q))) and isPrime(int(str(q) + str(p)))

def remarkable(p,q,_d={(7,3):True}):
	if (p,q) not in _d:
		_d[(p,q)] = isPrime(p*10**(numberOfDigits(q)) + q) and isPrime(q*10**(numberOfDigits(p)) + p)
	return _d[(p,q)]

def remarkable(p,q,_d={(7,3):True}):
	if (p,q) not in _d:
		_d[(p,q)] = isPrime(int(str(p) + str(q))) and isPrime(int(str(q) + str(p)))
	return _d[(p,q)]

def remarkablel(args):
	for pair in combinations(args,2):
		if not remarkable(*pair):
			return False
	return True

def problem60e():
	''' Past records:
[5381, 5507, 7877, 41621, 47237]
107623
>>> sum([7, 1237, 2341, 12409, 18433])
34427
'''
	record = 34427
	listOfPrimes = primesUpTo(18433)
	for index1, a in enumerate(listOfPrimes):
		for index2, b in enumerate(listOfPrimes[index1+1:]):
			if (a + b < 2/5*record) and remarkable(a,b):
				for index3, c in enumerate(listOfPrimes[index1+index2+2:]):
					if a + b + c < 3/5*record and remarkable(a,c) and remarkable(b,c):
						for index4, d in enumerate(listOfPrimes[index1+index2+index3+3:]):
							if a + b + c + d < 4/5*record and remarkable(a,d) and remarkable(b,d) and remarkable(c,d):						
								for e in listOfPrimes[index1+index2+index3+index4+4:]:
									if a + b + c + d + e < record and remarkable(a,e) and remarkable(b,e) and remarkable(c,e) and remarkable(d,e):
										return sum([a,b,c,d,e])


def problem60a():
	listOfPrimes = primesUpTo(18433)
	for index1, a in enumerate(listOfPrimes):
		for index2, b in enumerate(listOfPrimes[:index1]):
			if not remarkable(a,b): continue
			for index3, c in enumerate(listOfPrimes[:index2]):
				if not(remarkable(a,c) and remarkable(b,c)): continue
				for index4, d in enumerate(listOfPrimes[:index3]):
					if not (remarkable(a,d) and remarkable(b,d) and remarkable(c,d)): continue
					for e in listOfPrimes[:index4]:
						if not(remarkable(a,e) and remarkable(b,e) and remarkable(c,e) and remarkable(d,e)): continue
						return sum([a,b,c,d,e])


def problem60b():
	listOfPrimes = primesUpTo(10000)
	for index1, a in enumerate(listOfPrimes[3:]):
		for index2, b in enumerate(listOfPrimes[3:index1]):
			if not remarkable(a,b): continue
			for index3, c in enumerate(listOfPrimes[3:index2]):
				if not(remarkable(a,c) and remarkable(b,c)): continue
				for index4, d in enumerate(listOfPrimes[3:index3]):
					if not (remarkable(a,d) and remarkable(b,d) and remarkable(c,d)): continue
					for e in listOfPrimes[3:index4]:
						if not(remarkable(a,e) and remarkable(b,e) and remarkable(c,e) and remarkable(d,e)): continue
						return sum([a,b,c,d,e]), [a,b,c,d,e]

def concatenateWith(a,_d={2:set(),3:set(),5:set(),7:{3}}):
	if a not in _d:
		_d[a] = set()
		for p in primesUpTo(a):
			if remarkable(a,p):
				_d[a].add(p)
	return _d[a]

def problem60c():
	listOfPrimes = primesUpTo(10000)
	for a in listOfPrimes:
		for b in concatenateWith(a):
			for c in concatenateWith(b).intersection(concatenateWith(a)):
				for d in concatenateWith(c).intersection(concatenateWith(a)).intersection(concatenateWith(b)):
					for e in concatenateWith(d).intersection(concatenateWith(a)).intersection(concatenateWith(b)).intersection(concatenateWith(c)):
						return sum([a,b,c,d,e,])

def problem60d():
	listOfPrimes = primesUpTo(10000)
	for a in listOfPrimes:
		A = concatenateWith(a)
		for b in A:
			B = concatenateWith(b)
			for c in A.intersection(B):
				C = concatenateWith(c)
				for d in A.intersection(B).intersection(C):
					D = concatenateWith(d)
					for e in A.intersection(B).intersection(C).intersection(D):
						return sum([a,b,c,d,e,])

def concatenateWith(a,primes,_d={2:set(),3:set(),5:set(),7:{3}}):
	if a not in _d:
		_d[a] = set()
		for p in primes:
			if p == a: break
			if remarkable(a,p):
				_d[a].add(p)
	return _d[a]

def remarkable(p,q):#,_d={(7,3):True}):
	#if (p,q) not in _d:
	#	_d[(p,q)] = isPrime(int(str(p) + str(q))) and isPrime(int(str(q) + str(p)))
	return isPrime(int(str(p) + str(q))) and isPrime(int(str(q) + str(p)))

def problem60():
	listOfPrimes = []#primesUpTo(10000)
	for a in iPrime():
		listOfPrimes.append(a)
		A = concatenateWith(a,listOfPrimes)
		for b in A:
			B = concatenateWith(b,listOfPrimes).intersection(A)
			for c in B:
				C = concatenateWith(c,listOfPrimes).intersection(B)
				for d in C:
					D = concatenateWith(d,listOfPrimes).intersection(C)
					for e in D:
						return sum([a,b,c,d,e,])

if __name__ == "__main__":
	#print(problem60a())#==26033)
	print(problem60e())