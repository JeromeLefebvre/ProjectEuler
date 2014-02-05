

'''
Consider the infinite polynomial series AF(x) = xF1 + x2F2 + x3F3 + ..., where Fk is the kth term in the Fibonacci sequence: 1, 1, 2, 3, 5, 8, ... ; that is, Fk = Fk−1 + Fk−2, F1 = 1 and F2 = 1.

For this problem we shall be interested in values of x for which AF(x) is a positive integer.

Surprisingly AF(1/2)	 = 	(1/2).1 + (1/2)2.1 + (1/2)3.2 + (1/2)4.3 + (1/2)5.5 + ...
 	 = 	1/2 + 1/4 + 2/8 + 3/16 + 5/32 + ...
 	 = 	2
The corresponding values of x for the first five natural numbers are shown below.

x	AF(x)
√2−1	1
1/2	2
(√13−2)/3	3
(√89−5)/8	4
(√34−3)/5	5
We shall call AF(x) a golden nugget if x is rational, because they become increasingly rarer; for example, the 10th golden nugget is 74049690.

Find the 15th golden nugget.
'''

from itertools import combinations_with_replacement
from projectEuler import gcd, isSquare

nuggets = []
'''
for p,q in combinations_with_replacement(range(1,10000),2):
	if (p,q) != (1,1) and gcd(p,q) == 1:
		if p*q % (q**2 - p*q - p**2) == 0 and p*q // (q**2 - p*q - p**2) > 0:
			nuggets.append(p*q // (q**2 - p*q - p**2))
'''

def integerSquare(d):
	''' Expects a square integer '''
	s = int(sqrt(d))
	if d == s**2:
		return s
	return s+1

from math import sqrt

def solveQuadratic(a,b,c):
	disc = b**2 - 4*a*c
	soln = []
	if disc > 0:
		if isSquare(disc):
			d = integerSquare(disc)
			if (-b - d) % (2*a) == 0:
				soln.append((-b - d) // (2*a))
			if (-b + d) % (2*a) == 0:
				soln.append((-b + d) // (2*a))
	return soln

solveQuadratic(1,-11,30)				


GOAL = 10000000
for p in range(1,GOAL):
	#for q in [(-p + (p**2 - 4*(-p**2 + 1))**(1/2))/2, (-p + (p**2 - 4*(-p**2 - 1))**(1/2))/2, (-p - (p**2 - 4*(-p**2 + 1))**(1/2))/2, (-p - (p**2 - 4*(-p**2 - 1))**(1/2))/2]:
	for q in solveQuadratic(1,-p,-p**2 - 1):
		if q != 0:
			s = (p*q) // (q**2 - p*q - p**2)
			if s > 0:
				if s not in nuggets:
					nuggets.append(s)
	for q in solveQuadratic(1,-p,-p**2 + 1):
		if q != 0:
			s = (p*q) // (q**2 - p*q - p**2)
			if s > 0:
				if s not in nuggets:				
					nuggets.append(s)
	if len(nuggets) == 15:
		break

nuggets.sort()
print(nuggets[-1])












