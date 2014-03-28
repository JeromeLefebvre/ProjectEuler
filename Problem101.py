#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=101
Optimum polynomial
Problem 101
'''

'''
Notes on problem 101():
'''


def polynomialFromValues2(values = [(0,0),(1,1)]):
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
		print(total, total.numerator)
		return total.numerator
	return p
	
def problem1012():
	def u(n): return sum([ (-1)**i*n**i for i in range(0,11)])
	#def u(n): return n**3
	total = 0
	for n in range(1,13):	
		p = polynomialFromValues([ (i, u(i)) for i in range(1,n+1) ] )
		if p(n+1) != u(n+1):
			total += p(n+1)
	return total

def polynomialFromValues(values):
	''' computes p(n) the polynomial interpretation of the given pairs'''
	# Using fractions as a way to handle loss of accuracy
	#from fractions import Fraction as F
	#values = [values[i] for i in range(0,len(values))]
	def p(n):
		total = 0
		ai = 0
		for value in values:
			ai += 1
			prodN = 1
			prodD = 1
			aj = 0
			for secondvalue in values:
				aj += 1
				if ai != aj:
					prodN *= (n - aj)
					prodD *= ai - aj
			total += value*prodN/(prodD)
		return int(total)
	return p
	
def problem101():
	def u(n): return sum([ (-1)**i*n**i for i in range(0,11)])
	#def u(n): return n**3
	total = 0
	for n in range(1,13):	
		p = polynomialFromValues([ u(i) for i in range(1,n+1) ] )
		#print(n,p(n))
		print(n+1,p(n+1))
		if p(n+1) != u(n+1):
			total += p(n+1)
	return total

from cProfile import run
if __name__ == "__main__":
	run("problem101()")
	print(problem101() == 37076114526)
 