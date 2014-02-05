#!/usr/local/bin/python3.3
'''
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

from PE_sequences import triangle as sumsOfFirstIntegers

def problem1():
	# Need to remove 1 since we aren't including 1000
	GOAL = 1000-1
	# Inclusion/exclusion
	# Find all the multiples of 3, 5 and 15
	# then sum up all the 3s and 5s then remove the comons 15
	multiplesOf3 = 3*sumsOfFirstIntegers(GOAL//3)
	multiplesOf5 = 5*sumsOfFirstIntegers(GOAL//5)
	multiplesOf15 = 15*sumsOfFirstIntegers(GOAL//15)
	return multiplesOf3 + multiplesOf5 - multiplesOf15

import cProfile
if __name__ == "__main__":
	print(problem1() == 233168)
	cProfile.run("problem1()")