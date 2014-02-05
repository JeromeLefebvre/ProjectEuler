#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=66()
Diophantine equation
Problem 66
Consider quadratic Diophantine equations of the form:

x2 – Dy2 = 1

For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

3^2 – 2×2^2 = 1
2^2 – 3×1^2 = 1
9^2 – 5×4^2 = 1
5^2 – 6×2^2 = 1
8^2 – 7×3^2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.
'''

'''
Notes on problem 66():
'''
from projectEuler import isSquare
from PE_quadratics import pell
from math import sqrt


def problem66():
	return max([(pell(D),D) for D in range(1,1000) if not isSquare(D)])[1]

from cProfile import run
if __name__ == "__main__":
	print(problem66() == 661)
	run("problem66()")
 