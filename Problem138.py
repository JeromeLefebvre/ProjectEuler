#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=138
Special isosceles triangles
Problem 138
'''

'''
Notes on problem 138():
'''

from quadratics import isSquare
def aSolution(b):
	for h in [b-1,b+1]:
		if isSquare( (b//2)**2 + h**2 ):
			return True
	return False

from itertools import count
from PE_primes import factorize
def problem138():
	total = 0
	found = 0
	for b in count(0,2**4):
		if aSolution(b):
			print(b,factorize(b))
			found += 1
		if found == 12:
			break



from cProfile import run
if __name__ == "__main__":
	#run("problem138()")
	print(problem138()) 