#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=134
Prime pair connection
Problem 134
'''

'''
Notes on problem 134():
'''

from PE_digits import numberOfDigits
from PE_primes import primesUpTo
def smallest(p1,p2):
	l = numberOfDigits(p1)
	inv = pow(10**l,p2-2,p2)
	r = (-inv*p1) % p2
	return r*10**l + p1

def problem134():
	total = 0
	primes = primesUpTo(1000100)
	for index, p1 in enumerate(primes):
		if p1 == 2 or p1 == 3: continue
		if p1 > 1000000: break
		p2 = primes[index+1]
		total += smallest(p1, p2)
	return total
	


from cProfile import run
if __name__ == "__main__":
	#run("problem134()")
	print(problem134()) 