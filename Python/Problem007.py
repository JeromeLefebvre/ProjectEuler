#!/usr/local/bin/python3.3

'''
10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

from pe.primes import iPrime, primesUpTo

def problem7():
	''' We have a crude bound on the number of primes given by x/ln(x)
	Thus we need 10001 < x/ln(x) and 200000 works'''
	primes = primesUpTo( 200000)
	return primes[10001-1]

def problem7a():
	''' solution using an iterator '''
	for index,p in enumerate(iPrime()):
		if index + 1 == 10001:
			return p

from cProfile import run
if __name__ == "__main__":
	print(problem7() == 104743)
	print(problem7a() == 104743)
	run("problem7()")
	run("problem7a()")