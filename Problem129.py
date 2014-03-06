#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=129
Repunit divisibility
Problem 129
'''

'''
Notes on problem 129():
'''

from fractions import gcd

from itertools import count, dropwhile

from PE_primes import factorize

def A(n):
	assert(gcd(n,10) == 1)
	for k in count(2):
		if pow(10,k,9*n) == 1:
			return k

def A(n):
	#assert(gcd(n,10) == 1)
	o = pow(10,1,9*n)
	count = 1
	while not (o == 1):
		o = pow(o*10,1,9*n)
		count += 1
	return count 

# We notice that A(n) is greater than n.
def problem129():
	for n in count(10**6):
		if n % 2 == 0 or n%5 == 0: continue
		if A(n) > 10**6:
			return n


from cProfile import run
if __name__ == "__main__":
	#run("problem129()")
	print(problem129()) 