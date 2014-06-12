
from PE_primes import muUpTo_abs

def Q(n):
	''' Computes the number of square free numbers'''
	mu = muUpTo_abs(int(n**(1/2.0)))
	total = 0
	for d in range(1,int(n**(1/2.0))):
		total += mu[d]*int(n/(d**2))
	return total

#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=193
Squarefree Numbers
Problem 193

'''

'''
Notes on problem 193():
'''

def problem193():
	return Q(2**50)


from cProfile import run
if __name__ == "__main__":
	run("problem193()")
	print(problem193() == 684465067343069) 