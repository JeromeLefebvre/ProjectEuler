#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=115
Counting block combinations II
Problem 115
'''

'''
Notes on problem 115():
'''

def problem115():
	def numberOfSolutions(minlength,numBlocks,soFar=0,d={}):
		if (minlength,numBlocks) not in d:
			count = 1 # Everything is blank
			for length in range(minlength,numBlocks + 1): # we can have blocks of length 3 to max length
				for placement in range(0, numBlocks-length+1):
					count += numberOfSolutions(minlength, numBlocks - placement - length - 1)
			d[(minlength,numBlocks)] = count
		return d[(minlength,numBlocks)]
	from itertools import count
	for n in count():
		if numberOfSolutions(50,n) > 10**6:
			return n


from cProfile import run
if __name__ == "__main__":
	run("problem115()")
	print(problem115()) 