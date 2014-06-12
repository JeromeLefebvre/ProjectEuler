#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=152
Writing 1/2 as a sum of inverse squares
Problem 152
'''

'''
Notes on problem 152():
'''

from fractions import Fraction as F
def problem152():
	remainding = {i: sum([F(1,j**2) for j in range(i+1,46)]) for i in range(2,47)} # The sum of all the tail
	print("starting")
	count = 0

	def find(i=3,sofar=F(1,2**2)):
		if i == 11 or i == 10: print(str(i))
		if sofar == F(1,2):
			print("foundOne")
			return
		if i >= 46:
			return
		if sofar + remainding[i-1] < F(1,2):
			return
		if sofar + F(1,i**2) <= F(1,2): #add in the current term
			find(i+1, sofar + F(1,i**2))
		find(i+1, sofar) # skip the current term
	find()
	return count

from functools import lru_cache

@lru_cache(maxsize=100)
def remainingSum(i):
	return sum([1/j**2 for j in range(i+1, 45+1)])


@lru_cache(maxsize=10**6)
def search(i, partial):
	if partial == 1/2:
		return 1
	if partial > 1/2:
		return 0
	remaining = remainingSum(i)
	if remaining + partial < 1/2:
		return 0
	total = 0
	for j in range(i+1, 45+1):
		total += search(j, partial+1/j**2)
	return total 

def problem152():
	return search(2,1/2**2)


from cProfile import run
if __name__ == "__main__":
	#run("problem152()")
	print(problem152()) 