#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=101
Optimum polynomial
Problem 101
'''

'''
Notes on problem 101():
'''
from projectEuler import *

def polynomialFromValues(values = [(0,0),(1,1)]):
	''' computes p(n) the polynomial interpretation of the given pairs'''
	# Using fractions as a way to handle loss of accuracy
	from fractions import Fraction as F
	def p(n):
		total = 0
		for pair in values:
			prod = F(1,1)
			xi = F(pair[0],1)
			yi = F(pair[1],1)
			for secondPair in values:
				xj = F(secondPair[0],1)
				if xi != xj:
					prod *= (n - xj)/(xi-xj)
			total += yi*prod
		return total.numerator
	return p

def problem101():
	def u(n): return sum([ (-1)**i*n**i for i in range(0,11)])
	#def u(n): return n**3
	total = 0
	for n in range(1,13):	
		p = polynomialFromValues([ (i, u(i)) for i in range(1,n+1) ] )
		if p(n+1) != u(n+1):
			total += p(n+1)
	return total
	
	

if __name__ == "__main__":
	print(problem101())
 