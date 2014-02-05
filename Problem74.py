#!/usr/local/bin/python3.3

'''

Problem 74
The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
'''

'''
Notes on problem 74():
Should add a way to store computed lengths to speed up the algorithm
'''
from math import factorial

#def applyToDigits(n,function):
#	return sum([function(int(a)) for a in str(n)])

#def f(n):
#	return sum([factorial(int(a)) for a in str(n)])

def chainLength(n):
	from PE_digits import applyToDigits
	seen = []
	while n not in seen:
		seen.append(n)
		n = applyToDigits(n,factorial)
	#print(seen)
	return len(seen)

def problem74a():
	count = 0
	for i in range(1,10**6):
		if chainLength(i) == 60:
			count += 1
	return count

def chain(n,_d={1:1}):
	def f(n): return applyToDigits(n,factorial)
	from PE_digits import applyToDigits
	if n in _d:
		return n
	seen = []
	while n not in seen:
		seen.append(n)
		n = f(n)
	entrance = seen.index(n)
	lengthOfLoop = len(seen) - entrance
	for i in range(0,lengthOfLoop):
		_d[seen[entrance + i]] = lengthOfLoop
	for i in range(0,entrance):
		_d[seen[i]] = lengthOfLoop + (entrance - i)
	return len(seen)

def chain(n,_d={1:1}):
	def f(n): return applyToDigits(n,factorial)
	from PE_digits import applyToDigits
	if n in _d:
		return _d[n]
	seen = []
	while n not in seen:
		seen.append(n)
		n = f(n)
		if n in _d:
			for i in range(0,len(seen)):
				_d[seen[i]] = len(seen) - i + _d[n]
			return _d[seen[0]]
	# we've completed a full loop
	if n in seen:
		entrance = seen.index(n)
		lengthOfLoop = len(seen) - entrance
		for i in range(0,lengthOfLoop):
			_d[seen[entrance + i]] = lengthOfLoop
		for i in range(0,entrance):
			_d[seen[i]] = lengthOfLoop + (entrance - i)
	return _d[seen[0]]

def problem74():
	count = 0
	for i in range(1,10**6):
		if chain(i) == 60:
			count += 1
	return count

def problem74b():
	for n in range(1,10**6):
		if chainLength(n) != chain(n):
			return n

from cProfile import run
if __name__ == "__main__":
	print(problem74() == 402)
	run("problem74()")
	print(problem74a() == 402)
	run("problem74a()")
	#print(problem74b())
 