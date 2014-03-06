
'''
Problem 23

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

from projectEuler import generateFactors,isAbudantFromFactors
from itertools import combinations_with_replacement
from PE_factors import genFactors
from MillerRabin import isPrime
from itertools import chain, combinations

def d(n):
	''' A fast version of sigma(n,1), does not work for large n'''
	# We already acount for the trivial divisors 1
	sigma = 1
	# We only need to check for divisors up to √n
	m  = n ** 1/2
	# If n is a square, we are over overcounting it
	if m == int(m): sigma -= int(m)
	m = int(m) + 1
	for i in range(2, m):
		# For every divisor, we get a pair of divisors
		if n % i == 0: sigma += i + n//i
	return sigma

def isAbudant(n):
	return d(n) > n

def problem23():
	# The first few numbers are easily cases
	abundantNumbers = {12,18,20}
	total = 24*(23)/2 + 20161
	# http://mathworld.wolfram.com/AbundantNumber.html
	# Every number greater than 20161 can be expressed as a sum of two abundant numbers
	for n in range(24,20161):
		# only numbers divisible by 2 or 3 are abundant for small numbers
		# A number that is divisible by 6 is abundant
		if not (n%6 in {1,5}) and (n%6 == 0 or d(n) > n):
			abundantNumbers.add(n)
		if not any( n-j in abundantNumbers for j in abundantNumbers): total += n
	return total

def sigmaUpTo(n):
	sigmas = [1] * (n+1)
	for i in range(2, int(n**(1/2))+1):
		sigmas[i*i] += i
		for k in range(i+1, n//i+1):
			sigmas[k*i] += k+i
	return sigmas

def problem23():
	sigmas = sigmaUpTo(20161)
	abundantNumbers = {12,18,20}
	total = sum([i for i in range(1,24)]) + 20161
	for n in range(24,20161):
		if sigmas[n] > n:
			abundantNumbers.add(n)
		if not any( n-j in abundantNumbers for j in abundantNumbers): total += n
	return total

from cProfile import run
if __name__ == "__main__":
	print(problem23() == 4179871)
	run("problem23()")
	print(problem23a() == 4179871)
	run("problem23a()")	

