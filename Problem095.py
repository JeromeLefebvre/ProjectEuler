#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=95
Amicable chains
Problem 95
The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding one million.
'''

'''
Notes on problem 95():
'''
from projectEuler import divisors

def sigma(n,_d={1:1}):
	''' Returns the sum of the divisors of a number minus the number itself'''
	if n in _d:
		return _d[n]
	div = divisors(n)
	_d[n] = sum(a for a in div) - max(div)
	return _d[n]

def problem95():
	record = 0
	recordChain = []
	for n in range(1,10**6):
		chain = []
		intital = n
		while n < 10**6 and n not in chain:
			chain.append(n)
			n = sigma(n)
		#if n == 12496: print(chain)
		if len(chain) > record and n == chain[0]:
			record = len(chain)
			recordChain = chain
			print(chain)
	return min(recordChain), recordChain



if __name__ == "__main__":
	print(problem95())
 