#!/usr/local/bin/python3.3

'''
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

from PE_primes import divisors

def problem9():
	''' We know that a + b + c = 2*m**2 + 2*m*n thus 2m divides 1000 or m is a divisor of 500'''
	for m in divisors(500):
		for n in range(1,m):
			a = m**2 - n**2
			b = 2*m*n
			c = m**2 + n**2
			if  m**2 + m*n == 500:
				return a*b*c

def problem9a():
	''' The naive approach works quickly quickly enough '''
	for a in range(1,1000):
		for b in range(1,a):
			c = 1000 - a - b
			if a**2 + b**2 == c**2:
				return a*b*c

from cProfile import run
if __name__ == "__main__":
	print(problem9() == 31875000)
	print(problem9a() == 31875000)
	run("problem9()")
	run("problem9a()")