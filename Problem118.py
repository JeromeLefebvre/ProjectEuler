#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=118
Pandigital prime sets
Problem 118
'''

'''
Notes on problem 118():
'''
def powerset(A,nonTrivial=False):
	''' powerset(set) -> iterator -- returns a complete list of all subsets of A as tuple, if nonTrivial=True, returns all set expects the empty set and A'''
	from itertools import chain, combinations
	if nonTrivial:
		return chain.from_iterable( combinations(A,i) for i in range(1,len(A)) )
	else:	
		return chain.from_iterable( combinations(A,i) for i in range(0,len(A)+1) )

## IMPROVE:
# We should only need to go over first subsets that contain 1
# Then subsets that include the first digits to avoid so much repetition.
from itertools import permutations
from PE_primes import isPrime
def problem118():
	seen = set()
	def allPrimes(digits,soFar=set()):
		if len(digits) == 0:
			seen.add(tuple(sorted(tuple(soFar))))
			print(len(seen))
		else:
			for combi in powerset(digits):
				if combi == (): continue
				for perm in permutations(combi, len(combi)):
					number = int(''.join([str(s) for s in perm]))
					if isPrime(number):
						allPrimes(digits.difference(perm), soFar.union({number}))
	allPrimes({1,2,3,4,5,6,7,8,9})
	print(len(seen))

from cProfile import run
if __name__ == "__main__":
	run("problem118()")
	print(problem118()) 