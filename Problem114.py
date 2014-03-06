#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=114
Counting block combinations I
Problem 114
'''

'''
Notes on problem 114():
'''

def problem114():
	def numberOfSolutions(numBlocks, d={}):
		if numBlocks not in d:
			count = 1 # Everything is blank
			for length in range(3,numBlocks + 1): # we can have blocks of length 3 to max length
				for placement in range(0, numBlocks-length+1):
					count += numberOfSolutions(numBlocks - placement - length - 1)
			d[numBlocks] = count
		return d[numBlocks]
	return numberOfSolutions(50)


from cProfile import run
if __name__ == "__main__":
	run("problem114()")
	print(problem114()) 