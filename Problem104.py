#!/usr/local/bin/python3.3

'''
Pandigital Fibonacci ends
Problem 104
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
It turns out that F541, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order). And F2749, which contains 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.
'''

'''
Notes on problem 104():
'''
from projectEuler import iFibonacci,primes

def genLast10Fib():
	''' An interator for the Fibonacci sequence 1,2,3,5'''
	a,b = 1,2
	yield a
	yield b
	while True:
		yield b % 10**10
		a,b = b % 10**10, (a+b)%10**10

from math import sqrt,log

def isPandigital(n):
	return set(str(n)) == {'1','2','3','4','5','6','7','8','9'} and len(str(n)) == 9
def top_digits(n):
  # t = n * log10(phi)          + log10(1/sqrt(5))
  # Using log() seem to break the accurracy
  t = n * 0.20898764024997873 + (-0.3494850021680094)
  t = int((pow(10, t - int(t)))*10**8)
  return t

def problem104():
	c = primes()
	memo={0:0, 1:1}
	for k, F in enumerate(genLast10Fib()):
		if isPandigital(F):
			a = top_digits(k+1)
			if isPandigital(a):
				return k + 1
		if k+2 > 329468:
			break
	
if __name__ == "__main__":
	print(problem104())

 