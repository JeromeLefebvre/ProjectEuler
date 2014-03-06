#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=171
Finding numbers for which the sum of the squares of the digits is a square
Problem 171
'''

'''
Notes on problem 171():
'''

def f(l):
	return sum([i**2 for i in l])

def isSquare(n):
	return int(n**(1/2))**2 == n

from itertools import count, combinations_with_replacement

def problem171():
	for l in combinations_with_replacement(range(0,10),19):
		if isSquare(f(l)):
			print(l)


from cProfile import run
if __name__ == "__main__":
	#run("problem171()")
	print(problem171()) 