#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=266
Pseudo Square Root
Problem 266
'''

'''
Notes on problem 266():
'''

from PE_basic import powerset,product
from PE_primes import primesUpTo

def productMod(c,mod=10**6):
	prod = 1
	for a in c:
		prod *= a
		prod %= mod
	return mod

def PSR(primes):
	return max([ product(c) for c in powerset(primes) if product(c) < product(primes)**(1/2) ])

def problem266():
	return PSR( primesUpTo(190) ) % 10**6


from cProfile import run
if __name__ == "__main__":
	#run("problem266()")
	print(problem266()) 