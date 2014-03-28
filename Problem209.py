#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=209
Circular Logic
Problem 209
'''

'''
Notes on problem 209():
'''

from itertools import product
from copy import copy

space = [p for p in product([0,1],[0,1],[0,1],[0,1],[0,1],[0,1])]
functions = [p for p in product([0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1])]

def problem209():
	space = [p for p in product([0,1],[0,1],[0,1],[0,1],[0,1],[0,1])]
	total = 0
	def forced(p):
		# p = (a,b,c)
		a,b,c,d,e,f = p
		return b,c,d,e,f,a^(b&c)

	def seek(soFar={(0,0,0,0):0}):
		total = 1
		for p in space: # loop over all possible asignments
			if p in soFar: continue
			# We set this new candidate to assign 1 on p
			q = forced(p)
			if q not in soFar:
				nextSolution = copy(soFar)
				nextSolution[p] = 1
				nextSolution[q] = 0
				total += seek(nextSolution)
		return total

	return seek()


from cProfile import run
if __name__ == "__main__":
	#run("problem209()")
	print(problem209()) 