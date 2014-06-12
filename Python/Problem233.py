#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=233()
Lattice points on a circle
Problem 233
Let f(N) be the number of points with integer coordinates that are on a circle passing through (0,0), (N,0),(0,N), and (N,N).

It can be shown that f(10000) = 36.

What is the sum of all positive integers N ≤ 1011 such that f(N) = 420 ?
'''

'''
Notes on problem 233():
'''
from projectEuler import primes, rwh_primes2

def numberOfSolutions(factors):
	R = 4
	for p in set(factors):
		if p % 4 == 1:
			R *= factors.count(p) + 1
	return R


def problem233():
	checker = primes(save=True, initial=False)
	checker.cleanup()

	print(numberOfSolutions(checker.factors(2*10000)))
	print(checker.factors(10000))



if __name__ == "__main__":
	print(problem233())
 