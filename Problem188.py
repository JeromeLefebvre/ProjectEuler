#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=188
The hyperexponentiation of a number
Problem 188
'''

'''
Notes on problem 188():
'''

import sys
sys.setrecursionlimit(2000)

def f(e,p):
	return pow(e,p,1855)

def doubleArrow(a,b,mod):
	if b == 1:
		return a
	else:
		return pow(a,doubleArrow(a,b-1,mod),mod)

def problem188():
	# starting from 8 the value of doubleArrow(1777,_,10**8) doesn't change.
	return doubleArrow(1777,8,10**8)


from cProfile import run
if __name__ == "__main__":
	#run("problem188()")
	print(problem188() == 95962097) 