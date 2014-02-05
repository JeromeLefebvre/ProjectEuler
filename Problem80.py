#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=80()
Square root digital expansion
Problem 80
It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
'''

'''
Notes on problem 80():
'''
from projectEuler import applyToDigits, isSquare, applyToDigits

from decimal import *

#def decimalSum(n):
#	return sum([int(b) for b in str(n)])

def problem80():
	getcontext().prec = 102
	total = 0
	for a in range(2, 100):
		if not isSquare(a):
			b = Decimal(a).sqrt()
			#total += applyToDigits(int(b * 10**100), lambda x: x)
			total += sum(int(c) for c in str(b * 10**100)[:100])
	return total

if __name__ == "__main__":
	print(problem80())
 