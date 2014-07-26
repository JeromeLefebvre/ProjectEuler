#!/usr/local/bin/python3.3

'''
Sum square difference
Problem 6
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

from pe.sequences import triangle, sumOfSquares

def problem6():
	return triangle(100)**2 - sumOfSquares(100)

from cProfile import run
if __name__ == "__main__":
	print(problem6() == 25164150)
	run("problem6()")