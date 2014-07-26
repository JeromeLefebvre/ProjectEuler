

'''
http://projecteuler.net/problem=35

Circular primes
Problem 35
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

from pe.digits import numberOfDigits
from pe.primes import primesUpTo

def cyclicShift(n):
	return n//10 + (n % 10)*10**(len(str(n)) -1)

def iCyclicShifts(n):
	''' Generates all cyclic shift, but doesn't yield n'''
	shift = cyclicShift(n)
	m = numberOfDigits(n) - 1
	while shift != n:
		yield shift
		shift = shift//10 + (shift % 10)*10**m

def isMadeOfOdd(n):
	while n > 0:
		if n % 10 not in {1,3,5,7,9}:
			return False
		n //= 10
	return True

def problem35():
	from PE_primes import primesUpTo, isPrime
	# count is 1 is we are not count 2 later
	count = 1
	# remove all primes that contain an even number, since those will have a cyclic shift that is even
	primesList = {p for p in primesUpTo(10**6) if isMadeOfOdd(p)}
	for p in primesList:
		if all(q in primesList for q in iCyclicShifts(p)):
			count += 1
	return count


if __name__ == "__main__":
	print(problem35() == 55)
	from cProfile import run
	run("problem35()")
