#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=231
The prime factorisation of binomial coefficients
Problem 231
'''

'''
Notes on problem 231():
'''

from PE_primes import factorize
def problem231():
	n = 20000000
	c = 15000000
	total = 0
	for m in range(n,n-c,-1):
		print(m)
		total += sum(factorize(m))
	for m in range(c,1,-1):
		print(-m)
		total -= sum(factorize(m))
	return total

from factorGenerating import genFactors
from PE_basic import product
def problem231():
	n = 20000000
	c = 15000000
	total = 1
	for factor in genFactors(n):
		prod = product(factor)		
		if n - c < prod <= n:
			total += sum(factor)
		if 1<= prod <= c:
			total -= sum(factor)
	return total 

#7526965179680
#18123831459749
from cProfile import run
if __name__ == "__main__":
	#run("problem231()")
	print(problem231()) 