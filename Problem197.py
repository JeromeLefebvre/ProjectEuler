#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=197()
Investigating the behaviour of a recursively defined sequence
Problem 197
Given is the function f(x) = ⌊230.403243784-x2⌋ × 10-9 ( ⌊ ⌋ is the floor-function),
the sequence un is defined by u0 = -1 and un+1 = f(un).

Find un + un+1 for n = 1012.
Give your answer with 9 digits after the decimal point.
'''

'''
Notes on problem 197():
'''
from projectEuler import primes
from decimal import *

def problem197():
	getcontext().prec = 20
	u = Decimal(-1)
	def f(x): return int(2**(Decimal(30.403243784)-x**2)) * Decimal(10**(-9))
	while abs(u - f(f(u)))>10**(-12):
		u = f(u)
	return float(str(u + f(u))[0:11])

if __name__ == "__main__":
	print(problem197())
 