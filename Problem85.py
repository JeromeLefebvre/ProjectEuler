#!/usr/local/bin/python3.3

'''
Counting rectangles
Problem 85
By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:


Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.
'''

'''
Notes on problem 85():
'''
from projectEuler import primes

def numberOfSquares(x,y):
	total = 0
	for a in range(1,x+1):
		for b in range(1,y+1):
			total += (x - a + 1)*(y - b + 1)
	return total

def problem85():
	record = 1000000000000
	xy = 1
	for x in range(1,200):
		for y in range(1,200):
			r = numberOfSquares(x,y)
			if abs(2*10**6 - r) < record:
				record = abs(2*10**6 - r)
				xy = x*y
	return xy

if __name__ == "__main__":
	print(problem85())
 