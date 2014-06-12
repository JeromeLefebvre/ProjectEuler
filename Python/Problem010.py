#!/usr/local/bin/python3.3

'''
Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from PE_primes import primesUpTo
def problem10():
	return sum(primesUpTo(2*10**6))

from cProfile import run
if __name__ == "__main__":
	print(problem10() == 142913828922)
	run("problem10()")