#!/usr/local/bin/python3.3

'''
Problem 16
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
'''

from PE_digits import applyToDigits

def problem16():
	return applyToDigits(2**1000)

from cProfile import run
if __name__ == "__main__":
	print(problem16() == 1366)
	run("problem16()")
 
