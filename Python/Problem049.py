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
from itertools import combinations

def sameDigits(a,b):
	return sorted([i for i in str(a)]) == sorted([i for i in str(b)])

def problem49a():
	checker = primes()
	for a in checker[1487:10000]:
		# the bound comes from wanting c = 2b - a ≤ 10000
		for b in checker[a:(10000+a)/2]:
			c = b + (b-a)
			# Do the same digits first since I think that is the most time consuming part
			if sameDigits(a,b) and sameDigits(b,c) and c in checker[1000:10000]:
				return int(str(a)+str(b) + str(c))

def sameDigits(a,b):
	''' sameDigits(int,int) -> bool -- returns True if and only if a and b are permutations of each other'''
	from collections import defaultdict
	d = defaultdict(int)
	for l in str(a):
		d[l] += 1   # Look Ma, no initializing!
	for l in str(b):
		d[l] -= 1
	# Check if I'm left with anything
	return not any(d.values())

# Can easily make this better
def problem49():
	from PE_primes import primesUpTo, isPrime
	from itertools import dropwhile
	primes = primesUpTo(10000)
	for a in dropwhile(lambda x : x <= 1487, primes):
		# the bound comes from wanting c = 2b - a ≤ 10000
		for b in dropwhile(lambda x : x <= a, primes):
			if b >= (10000 + a)/2: break
			c = b + (b-a)
			# Do the same digits first since I think that is the most time consuming part
			if sameDigits(a,b) and sameDigits(b,c) and isPrime(c):
				return int(str(a) + str(b) + str(c))

from cProfile import run
if __name__ == "__main__":
	run("problem49()")
	print(problem49() == 296962999629)