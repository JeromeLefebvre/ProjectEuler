#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=162
Hexadecimal numbers
Problem 162
'''

'''
Notes on problem 162():
'''

from PE_basic import nCk

def problem162():
	total = 0
	for n in range(3,17):
		 total +=15 * 16**(n - 1) + 41 * 14**(n - 1) - (43 * 15**(n - 1) + 13**n)
	return hex(total)[2:].upper()


from cProfile import run
if __name__ == "__main__":
	print(problem162())
	run("problem162()")
 
 