#!/usr/local/bin/python3.3

'''
Problem 61
Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate (polygonal) numbers and are generated by the following formulae:

Triangle	 	P3,n=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Square	 	P4,n=n2	 	1, 4, 9, 16, 25, ...
Pentagonal	 	P5,n=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	P6,n=n(2n−1)	 	1, 6, 15, 28, 45, ...
Heptagonal	 	P7,n=n(5n−3)/2	 	1, 7, 18, 34, 55, ...
Octagonal	 	P8,n=n(3n−2)	 	1, 8, 21, 40, 65, ...
The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties.

The set is cyclic, in that the last two digits of each number is the first two digits of the next number (including the last number with the first).
Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and pentagonal (P5,44=2882), is represented by a different number in the set.
This is the only set of 4-digit numbers with this property.
Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.
'''

'''
Notes on problem 61():
'''
from PE_sequences import iPentagonal, iHexagonal, iTriangle,iSquare,iHeptagonal,iOctagonal

from itertools import product, permutations
def problem61():
	pentagonal = {a for a in iPentagonal(10000) if a > 999}
	hexagonal = {a for a in iHexagonal(10000) if a > 999}	
	triangle = {a for a in iTriangle(10000) if a > 999}	
	square = {a for a in iSquare(10000) if a > 999}
	heptagonal = {a for a in iHeptagonal(10000) if a > 999}
	octagonal = {a for a in iOctagonal(10000) if a > 999}
	
	allData = [triangle,pentagonal,hexagonal,square,heptagonal,octagonal]
	unique = [[]]*6
	for indexA, A in enumerate(allData):
		unique[indexA] = A
		for indexB, B in enumerate(allData):
			if indexA != indexB:
				unique[indexA].difference(B)

	for P in permutations([i for i in range(0,6)]):
		for a in unique[P[0]]:
			for b in unique[P[1]]:
				if a % 100 == b // 100:
					for c in unique[P[2]]:
						if b % 100 == c // 100:
							for d in unique[P[3]]:
								if c % 100 == d // 100:
									for e in unique[P[4]]:
										if d % 100 == e // 100:
											for f in unique[P[5]]:
												if e % 100 == f // 100 and f % 100 == a//100:
													return a + b + c + d + e + f

from cProfile import run
if __name__ == "__main__":
	print(problem61())
	run("problem61()")
 