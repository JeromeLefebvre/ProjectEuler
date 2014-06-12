#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=86
Cuboid route
Problem 86

'''

'''
Notes on problem 86():
'''

from itertools import permutations
from fractions import gcd
def problem86():
	from math import sqrt
	M, c, a = 1000000, 0, 2
	while c < M:
	    a += 1
	    for bc in range(3, 2*a):
	        if (bc*a) % 12 == 0:
	            s = sqrt(bc*bc + a*a)
	            if not s % 1:    #check if s is an perfect square (integer)
	                c += min(bc, a+1) - (bc+1)//2 
	return a

from cProfile import run
if __name__ == "__main__":
	run("problem86()")
	print(problem86())

 
 