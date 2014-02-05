#!/usr/local/bin/python3.3

'''
Problem 49
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

'''
Notes on problem 49():
'''
from projectEuler import primes
from itertools import combinations

def sameDigits(a,b):
	return set(str(a)) == set(str(b))

def problem49():
	checker = primes()
	for a in checker[1487:10000]:
		# the bound comes from wanting c = 2b - a ≤ 10000
		for b in checker[a:(10000+a)/2]:
			c = b + (b-a)
			# Do the same digits first since I think that is the most time consuming part
			if sameDigits(a,b) and sameDigits(b,c) and c in checker[1000:10000]:
				return int(str(a)+str(b) + str(c))

if __name__ == "__main__":
	print(problem49() == 296962999629)
