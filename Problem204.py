#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=204
Generalised Hamming Numbers
Problem 204
'''

'''
Notes on problem 204():
'''

from factorGenerating import genProducts
from PE_primes import primesUpTo
from PE_basic import product
def problem204():
	count = 1
	for a in genProducts(10**9,primesUpTo(100)):
		count += 1
	print(count)


from cProfile import run
if __name__ == "__main__":
	#run("problem204()")
	print(problem204()) 