'''
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

from pe.sequences import triangle as sumN

def problem1():
	GOAL = 1000-1 # below 1000
	# Inclusion/exclusion
	multiplesOf3 = 3*sumN(GOAL//3)
	multiplesOf5 = 5*sumN(GOAL//5)
	multiplesOf15 = 15*sumN(GOAL//15)
	return multiplesOf3 + multiplesOf5 - multiplesOf15

from cProfile import run
if __name__ == "__main__":
	run("problem1()")
	print(problem1() == 233168)
	