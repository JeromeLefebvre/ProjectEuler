#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=141()
Investigating progressive numbers, n, which are also square.
Problem 141
A positive integer, n, is divided by d and the quotient and remainder are q and r respectively. In addition d, q, and r are consecutive positive integer terms in a geometric sequence, but not necessarily in that order.

For example, 58 divided by 6 has quotient 9 and remainder 4. It can also be seen that 4, 6, 9 are consecutive terms in a geometric sequence (common ratio 3/2).
We will call such numbers, n, progressive.

Some progressive numbers, such as 9 and 10404 = 1022, happen to also be perfect squares.
The sum of all progressive perfect squares below one hundred thousand is 124657.

Find the sum of all progressive perfect squares below one trillion (1012).
'''

'''
Notes on problem 141():
'''
from projectEuler import isSquare

from fractions import Fraction as F
def isGeometricSequence(a,b,c):
	if a != 0 and b != 0 and c != 0:
		return any((F(a,b) == F(b,c), F(b,c) == F(c,a), F(b,a) == F(a,c)))
	return False

from math import sqrt
def isProgressive(n):
	for d in [d for d in range(2,int(sqrt(n))) if n % d != 0]:
		q = n// d
		r = n % d
		if isGeometricSequence(d,q,r): return True, d, q, r
	return [False]

from fractions import gcd
def problem141():
	#GOAL = 10**12
	GOAL = 10**12 # 623708737 = 10**9
	total = 0
	for a in range(2,int(GOAL**(1/3))):
		for b in [r for r in range(1,a) if (a**3*r + r**2 < GOAL and gcd(a,r) == 1)]:
			e,n = 1,0
			while n < GOAL:
				n = a**3*b*e**2 + e*b**2
				if isSquare(n):
					print(a,b,e)
					total += n
				e += 1
	return total




if __name__ == "__main__":
	print(problem141())
 