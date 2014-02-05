#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=203
Squarefree Binomial Coefficients
Problem 203
The binomial coefficients nCk can be arranged in triangular form, Pascal's triangle, like this:

1	
1		1	
1		2		1	
1		3		3		1	
1		4		6		4		1	
1		5		10		10		5		1	
1		6		15		20		15		6		1	
1		7		21		35		35		21		7		1
.........
It can be seen that the first eight rows of Pascal's triangle contain twelve distinct numbers: 1, 2, 3, 4, 5, 6, 7, 10, 15, 20, 21 and 35.

A positive integer n is called squarefree if no square of a prime divides n. Of the twelve distinct numbers in the first eight rows of Pascal's triangle, all except 4 and 20 are squarefree. The sum of the distinct squarefree numbers in the first eight rows is 105.

Find the sum of the distinct squarefree numbers in the first 51 rows of Pascal's triangle.
'''

'''
Notes on problem 203():
Booya a second in one shot
'''
from projectEuler import nCk, factorize

def isSquareFree(n):
	div = factorize(n)
	return len(div) == len(set(div))
def problem203():
	squarefree = set()
	for n in range(1,51):
		for k in range(1, n//2 + 1):
			if isSquareFree(nCk(n,k)):
				squarefree.add(nCk(n,k))
	return sum(squarefree) + 1


if __name__ == "__main__":
	print(problem203())
 