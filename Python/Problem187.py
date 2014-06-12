#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=187
Semiprimes
Problem 187
A composite is a number containing at least two prime factors. For example, 15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2 × 3.

There are ten composites below thirty containing precisely two, not necessarily distinct, prime factors: 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

How many composite integers, n < 108, have precisely two, not necessarily distinct, prime factors?
'''

'''
Notes on problem 187():
Boooya first shot
'''
from projectEuler import rwh_primes2
from factorGenerating import orderedlist

def problem187():
	GOAL = 10**8
	m = rwh_primes2(GOAL)
	primes = orderedlist(m)
	count = 0
	for p in m:
		if GOAL//p <= 1:
			break
		count += len(primes[p: GOAL//p])
	return count


if __name__ == "__main__":
	print(problem187())
 