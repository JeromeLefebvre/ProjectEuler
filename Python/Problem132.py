#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=132
Large repunit factors
Problem 132
'''

'''
Notes on problem 132():
'''

from PE_primes import iPrime
def problem132():
	found = []
	for p in iPrime():
		if pow(10,10**9,9*p) == 1:
			found.append(p)
		if len(found) == 40: break
	return sum(found)

from cProfile import run
if __name__ == "__main__":
	run("problem132()")
	print(problem132()) 