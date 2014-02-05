

'''
Problem 94
It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).
'''

'''
Found triangles
(5, 6)
(65, 66)
(901, 902)
(12545, 12546)

'''
from projectEuler import solveIntegerQuadratic, integerSquare

'''
squares = []
usefullSquares = []
for k in range(1,10**6):
	squares.append(k**2)
	if (k**2 - 4) % 3 == 0 and (k**2 - 4)//3 in squares:
		usefullSquares.append((k**2 - 4)//3)

total = 0
for d2 in usefullSquares:
	# 2l + 1, 2l+2 squares
	for a in solveIntegerQuadratic(3,-2,-1 -d2):
		if a > 0:
			if (a+1)*integerSquare(d2) % 4 == 0:
				print(a,a+1)
				total += 2*a + a+1

	for a in solveIntegerQuadratic(3,2,-1 -d2):
		if a - 1 > 0:
			if (a-1)*integerSquare(d2) % 4 == 0:
				print(a,a-1)				
				total += 2*a + a-1

print(total)

squares = []
for k in range(1,10**6):
	squares.append(k**2)
	if (k**2 - 4) % 3 == 0 and (k**2 - 4)//3 in squares:
		usefullSquares.append((k**2 - 4)//3)

total = 0
squares = []
for k in range(1,10**6):
	squares.append(k**2)
	if (k**2 - 4) % 3 == 0 and (k**2 - 4)//3 in squares:
		d2 = (k**2 - 4)//3
		for a in solveIntegerQuadratic(3,-2,-1 -d2):
			if a > 0:
				if (a+1)*integerSquare(d2) % 4 == 0 and 2*a + a+1 <= 10**12:
					print(a,a+1)
					total += 2*a + a+1
					print(total)

		for a in solveIntegerQuadratic(3,2,-1 -d2):
			if a - 1 > 0:
				if (a-1)*integerSquare(d2) % 4 == 0 and 2*a + a-11 <= 10**12:
					print(a,a-1)				
					total += 2*a + a-1
					print(total)
'''


#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=94
Almost equilateral triangles
Problem 94
'''

'''
Notes on problem 94():
'''
from projectEuler import *
from PE_quadratics import isSquare

def problem94():
	total = 0
	for a in range(1,10**6):
		#if (3*a**2 - 2*a - 1) % 4 == 0 and isSquare((3*a**2 - 2*a - 1)):
		if isSquare((3*a**2 - 2*a - 1)):
			p = 3*a + 1
			if p < 10**6:
				total += p
		#if (3*a**2 + 2*a - 1) % 4 == 0 and 
		if isSquare((3*a**2 + 2*a - 1)):
			p = 3*a - 1
			if p < 10**6:
				total += p		
	return total


from cProfile import run
if __name__ == "__main__":
	print(problem94())
	run("problem94()")
 
 