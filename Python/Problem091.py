#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=91
Right triangles with integer coordinates
Problem 91
The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and are joined to the origin, O(0,0), to form ΔOPQ.


There are exactly fourteen triangles containing a right angle that can be formed when each co-ordinate lies between 0 and 2 inclusive; that is,
0 ≤ x1, y1, x2, y2 ≤ 2.


Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?
'''

'''
Notes on problem 91():
'''
from projectEuler import primes
from fractions import gcd
def solutions(p,q):
	GOAL = 50
	g = gcd(p,q)
	upperBound = []
	# upper bound from x ≥ 0
	# if q = 0, no restrictions
	# else a ≤ gp/q
	if q != 0:
		upperBound.append(g*p // q)
	# upper bound from y <= 50
	# if p = 0, no restrictions as P is already below 50
	# else a ≤ gp/q		
	if p != 0:
		upperBound.append(g*(GOAL-q)//p)
	# We get twice by symmetry
	return min(upperBound)*2

def problem91():
	GOAL = 50
	# 
	count = GOAL**2 
	for p in range(0,GOAL + 1):
		for q in range(0, GOAL + 1):
			# we can ignore the origin
			if (p,q) != (0,0):
				count += solutions(p,q)
	return count 

if __name__ == "__main__":
	print(problem91())
 