#!/usr/local/bin/python3.3

'''
Problem 53
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr =	
n!
r!(n−r)!
,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?
'''

'''
Notes on problem 53():
'''
from pe.basic import nCk

def problem53():
	count = 0
	# 7 is a naive lower bound on nCk, i.e. cNk(n,k) ≥ (n/k)^k applying it to n = 2m, k = m we get this lower bound
	for n in range(7,100+1):
		# we can play similiar games on how small and how large k can be, but we do not get very good bounds
		for k in range(4,n-3):
			if nCk(n,k) >= 10**6:
				# we account for the entire row
				count += n - 2*k + 1
				break
	return count

def test():
	for m in range(2,15):
		print(m, (m+1)**m)

from cProfile import run
if __name__ == "__main__":
	print(problem53() == 4075)
	run("problem53()")	
 