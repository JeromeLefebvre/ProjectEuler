#!/usr/local/bin/python3.3

'''
Digit power sum
Problem 119
The number 512 is interesting because it is equal to the sum of its digits raised to some power: 5 + 1 + 2 = 8, and 83 = 512. Another example of a number with this property is 614656 = 284.

We shall define an to be the nth term of this sequence and insist that a number must contain at least two digits to have a sum.

You are given that a2 = 512 and a10 = 614656.

Find a30.
'''

'''
Notes on problem 119():
'''
from projectEuler import primes

def digitSum(n):
	return sum(int(a) for a in str(n))

def aPowerOfDigit(n):
	s = digitSum(n)
	exp = 1
	if s == 1:
		return False
	while s**exp < n:
		exp += 1
	return s**exp == n

def generatesNumbersFromPrimes(list):
	pass

def problem119():
	candidates = []
	seen = []
	for a in range(2,1000):
		for exp in range(2,20):
			if a**exp > 10:
				candidates.append((a,exp,a**exp))
	for a,exp,aexp in candidates:
		if digitSum(aexp)**exp == aexp:
			seen.append(aexp)
	seen.sort()
	return seen[30-1]
	seen = [81,512,2401,4913,5832,17576,19683,234256,390625,614656,1679616,17210368,34012224,52521875,60466176]
	for a in range(seen[-1]+1,10**8):
		if aPowerOfDigit(a):
			seen.append(a)
			print(a)
			if len(seen) == 30:
				return a
	




if __name__ == "__main__":
	print(problem119())
 