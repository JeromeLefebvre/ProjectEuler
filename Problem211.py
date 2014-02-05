#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=211
Divisor Square Sum
Problem 211
For a positive integer n, let σ2(n) be the sum of the squares of its divisors. For example,

σ2(10) = 1 + 4 + 25 + 100 = 130.
Find the sum of all n, 0 < n < 64,000,000 such that σ2(n) is a perfect square.
'''

'''
Notes on problem 211():
Well, brute force solved this one.
1922364685

[Finished in 8171.2s]
'''
from projectEuler import isSquare,sigma

def problem211():
	total = 0
	for n in range(1,64*10**6):
		if isSquare(sigma(n,2)):
			total += n
	return total



if __name__ == "__main__":
	print(problem211())
 