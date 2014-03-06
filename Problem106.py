#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=106
Special subset sums: meta-testing
Problem 106
'''

'''
Notes on problem 106():
'''

def nCk(n,k):
	from math import factorial as f
	if k > n:
		return 0
	return f(n)//(f(k)*f(n-k))

def setsOfSameSize(n,seen=[]):
	# Returns the number of ways to sets of the same cardinality that to NOT need to be compared
	# The only set that do not need to be compared at those of the form {x_i,x_j,...} < {y_i,y_j} where x_i < y_i, x_j < y_j, i.e.
	# for any elements in the first set, there is an element greater than it. So we encode this fact by a series of 101010, which means
	# out of a ordered list, we pick the 1st, 3rd and 5th to to be in the first set
	if seen.count(1) == n:
		return 1
	if seen.count(1) > seen.count(0):
		return setsOfSameSize(n,seen + [1]) + setsOfSameSize(n,seen + [0])
	else:
		return setsOfSameSize(n,seen + [1])

def numberToCompare(n):
	# We have all pairs of subsets n (//2 since we don't need to do the same comparison twice) - the # of sets that do not need to be compared
	return nCk(2*n,n)//2 - setsOfSameSize(n)

def problem106():
	n = 12
	total = 0
	for i in range(2,n//2+1):
		total += nCk(n,2*i)*numberToCompare(i)
	return total

from cProfile import run
if __name__ == "__main__":
	run("problem106()")
	print(problem106() == 21384) 