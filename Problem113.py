#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=113
Non-bouncy numbers
Problem 113
'''

'''
Notes on problem 113():
'''

from PE_basic import nCk

def increasingNumbers(n):
	# The world worst way to compute nCk(n+9,9)
	def find(leadingDigit=0, numberOfDigits=n):
		if numberOfDigits == 0:
			return 1
		return sum( find(i,numberOfDigits - 1) for i in range(leadingDigit,10) )
	return find()

def problem113():
	string = ""
	i = 100
	return nCk(i+9,9) + nCk(i + 10, 10) - 2 - 10*i

from cProfile import run
if __name__ == "__main__":
	#run("problem113()")
	print(problem113()) 