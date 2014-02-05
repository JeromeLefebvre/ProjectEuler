#!/usr/local/bin/python3.3


# DONE, solution is 134043

'''
http://projecteuler.net/problem=47()
## Needs improvements
Distinct primes factors
Problem 47
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
'''

'''
Notes on problem 47():
'''
#from projectEuler import primes

def problem47():
	checker = primes(save=True,initial=False)
	candidates = []
	i = 2
	while True:
		if len(set(checker.factors(i))) == 4:
			candidates.append(i)
			if len(candidates) == 4:
				return candidates[0]
		else:
			candidates = []
		i += 1


from PE_primes import factorize
from itertools import count
def problem47():
	candidates = []
	numbers = count()
	# Throw away zero
	next(numbers)
	for n in numbers:
		if len(set(factorize(n))) == 4:
			candidates.append(n)
			if len(candidates) == 4:
				return candidates[0]
		else:
			candidates = []

from cProfile import run
if __name__ == "__main__":
	print(problem47() == 134043)
	run("problem47()")