#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=164
Numbers for which no three consecutive digits have a sum greater than a given value
Problem 164
'''

'''
Notes on problem 164():
'''

def problem164():
	def noThrees(sofar=[]):
		if len(sofar) <= 0:
			return sum( noThrees(sofar + [i]) for i in range(1,10))
		if len(sofar) <= 1:
			return sum( noThrees(sofar + [i]) for i in range(0,10 - sofar[-1] + 1))
		if len(sofar) == 10:
			return 1
		return sum( noThrees(sofar + [i]) for i in range(0, 9 - sofar[-1] - sofar[-2] + 1))
	return noThrees()

from cProfile import run
if __name__ == "__main__":
	#run("problem164()")
	print(problem164()) 