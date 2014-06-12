#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=90
Cube digit pairs
Problem 90
'''

'''
Notes on problem 90():
'''
from projectEuler import *
from itertools import combinations,combinations_with_replacement

def d(a,b):
	return a*10 + b

def representsSquares(A,B):
	seen = set()
	if 6 in A:
		A += (9,)
	if 9 in A:
		A += (6,)
	if 6 in B:
		B += (9,)
	if 9 in B:
		B += (6,)	
	for a in A:
		for b in B:
			seen.add(a*10 + b)
			seen.add(b*10 + a)		
	return {n**2 for n in range(1,10)} <= seen

def problem90():
	count = 0
	seen = set()
	for dices in combinations_with_replacement( combinations([0,1,2,3,4,5,6,7,8,9],6), 2):
		#print(dices, representsSquares(*dices))
		if representsSquares(*dices):
			count += 1
	return count


from cProfile import run
if __name__ == "__main__":
	print(problem90() == 1217)
	run("problem90()")
 