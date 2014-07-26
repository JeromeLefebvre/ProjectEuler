#!/usr/local/bin/python3.3

'''
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

from pe.basic import lcmm

def problem5():
	return lcmm(range(1,20))

from cProfile import run
if __name__ == "__main__":
	print(problem5() == 232792560)
	run("problem5()")