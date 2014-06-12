#!/usr/local/bin/python3.3

'''
Amicable numbers
Problem 21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

from projectEuler import generateFactors
from itertools import combinations
from PE_factors import genFactors

from PE_basic import product
from PE_primes import divisors, sigma

# This is simply to see the speed of simply factoring all numbers 1 to 10000
def problem21():
	def d(n):
		return sigma(n, 1, proper=True)
	amicable = {}
	for n in range(1,10000):
		e = d(n)
		# we remove the friendly numbers
		if e != n:
			amicable[n] = e
	total = 0
	for key in amicable:
		try:
			if key == amicable[amicable[key]]:
				total+= key
		except:
			pass
	return total

def problem21a():
	def d(divisors):
		''' Returns the sum of the divisors of a number minus the number itself'''
		return sum(a for a in divisors) - max(divisors)
	numbers = []
	amicable = {}
	for c in genFactors(10000):
		div = divisors(c)
		n,dn = product(c), d(div)
		# we remove the friendly numbers
		if n != dn:
			amicable[n] = dn
	total = 0
	for key in amicable:
		try:
			if key == amicable[amicable[key]]:
				total+= key
		except:
			pass
	return total
	


from cProfile import run
if __name__ == "__main__":
	print(problem21()== 31626)
	run("problem21()")	
	print(problem21a()== 31626)
	run("problem21a()")
 

