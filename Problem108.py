#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=108()
Diophantine reciprocals I
Problem 108
In the following equation x, y, and n are positive integers.

1/x+1/y=1 /n
For n = 4 there are exactly three distinct solutions:

What is the least value of n for which the number of distinct solutions exceeds one-thousand?

NOTE: This problem is an easier version of problem 110; it is strongly advised that you solve this one first.


'''

'''
Notes on problem 108():

We are trying to find x such that xn/(x-n) = y.
That is x-n|xn and y is positve. First we need x > n for the positiviy (thus y > n) as well
For an upper bound, we note that as x grows the right hand side approaches n, thus we only need to count until
the right hand side is less than n+1 and this occurs at n**2 + n.
By symmetry we can assume x≥y we then get the further improvement in lower bound that x ≥ 2*n
This still runs dog slow. n that then to have a lot of solutions are products of low primes, 2,3,5,7,...
'''
'''
from projectEuler import primes,product

def generateFactorsFromList(n,checker,authorized,start=1,factors=[]):
	This generates all numbers between from 2 up to n as their list of factors
	if start <= n//product(factors):
		# The -1 is to make sure 2 is included when we are at 3
		for a in checker[start-1:n//product(factors)]:
			if set(factors + [a]) <= authorized:
				yield factors + [a]
			for c in generateFactorsFromList(n,checker,authorized,a,factors+[a]):
				if set(factors + [a]) <= authorized:
					yield c

def numberOfSolutions(n):
	return sum([ 1 for x in range(2*n, n**2 + n+1) if (x*n) % (x-n) == 0 ])

def solutions(n):
	sols = [ x for x in range(2*n, n**2 + n+1) if (x*n) % (x-n) == 0 ]
	for x in sols:
		y = (x*n) // (x-n)
		print(x,y,x % n,y%n)
	return all([x % n == 0 for x in sols])

solutions(2520)
def problem108():
	checker = primes()
	record = 0
	#for c in generateFactorsFromList(20000,checker,{2,3,5,7}):
	#	n = product(c)
	for n in range(4620,20000):
		if n % 2*2*2*2 == 0 and n%3 == 0:
			r = numberOfSolutions(n)
			if r > record:
				record = r
				print(n,r)
			if r > 1000:
				return n
			#print(n,r,checker.factors(n),solutions(n))
'''

from factorGenerating import genProducts
from projectEuler import product

def basicSolutions(n):
	count = 0
	for x in range(n+1,2*n+1):
		if x*n % (x - n) == 0:
			count += 1
	return count

from itertools import count
def problem108():
	recordN = 10**9
	recordSolutions = 0
	for n in genProducts(10**6,[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]):
		n = product(n)
		if n > 10:			
			m = basicSolutions(n)
			#if m >= 1000 and n < recordN:
			if m > recordSolutions:
				print(n,m)
				recordN = n
				recordSolutions = m
if __name__ == "__main__":
	print(problem108())
