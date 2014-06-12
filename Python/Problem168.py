#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=168
Number Rotations
Problem 168
'''

'''
Notes on problem 168():
'''

def rightShift(n):
	a = n%10
	b = n//10
	return a*10**(len(str(b))) + b

from itertools import count
from PE_primes import factorize

def problem168():
	power = 1
	for n in count(1):
		if n > 10**100:
			break
		if n >= 10**power:
			print("reached ", 10**power)
			power += 1
		if rightShift(n) % n == 0:
			if len(set(str(n))) != 1:
				print(n,factorize(rightShift(n)))


def problem168a():
	total = 0
	for n in count(1):
		if n > 230769:
			break
		if rightShift(n) % n == 0:
			total += n
	for digits in range(7,101):
		for i in range(1,10):
			total += int(str(i)*digits)
			#print(int(str(i)*digits))
			#total %= 10**5
	return total % 10**5

from cProfile import run
if __name__ == "__main__":
	#run("problem168()")
	print(problem168()) 