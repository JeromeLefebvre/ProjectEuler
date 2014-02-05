#!/usr/local/bin/python3.3

'''
Problem 75
It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?
'''

'''
Notes on problem 75():
'''
from projectEuler import integerSquare
from itertools import combinations

def numOfSolutions(n):
	count = 0
	for e in range(1,n//2):
		for b in range(1,n-e):
			if e**2 + b**2 == (n - e - b)**2:
				count += 1
	# somehow double counts
	return count//2


# 1000 221 600 seconds
def problem75a():
	solutions = {}
	GOAL = 1500000
	squaresTuple = [(n,n**2) for n in range(1,GOAL)]
	squares = [n**2 for n in range(1,GOAL)]
	for (a,a2),(b,b2) in combinations(squaresTuple,2):
		if a2 + b2 in squares:
			c = integerSquare(a2 + b2)
			if a2 + b2 in solutions:
				solutions[a + b + c] += 1
			else:
				solutions[a + b + c] = 1
	count = 0
	for i in solutions.keys():

		if solutions[i] == 1:
			count += 1
	return count

from fractions import gcd
def genPythagorianTriples():
	GOAL = 1500000
	result = 0
	triples = [0]*(GOAL+1)
	for m in range(1, int((GOAL/2)**1/2)+1):
		for n in range(1,m+1):
			if (m-n)%2 == 1 and gcd(m,n) == 1:
				p = 2*m**2 + 2*m*n
				# continuing will only increase n and will lead to a larger number
				if p > GOAL+100:
					break
				while p <= GOAL:
					triples[p] += 1
					if (triples[p] == 1): result += 1
					if (triples[p] == 2): result -= 1
					p += 2*m**2 + 2*m*n
	return result

def problem75():
	count = 0
	return genPythagorianTriples()
	return d.count(1)

from cProfile import run
if __name__ == "__main__":
	print(problem75() == 161667)
	run("problem75()")