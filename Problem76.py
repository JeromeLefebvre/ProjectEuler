#!/usr/local/bin/python3.3

'''
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
'''

'''
Notes on problem 76():
'''

def numberOfWays(n,maximum=None,d={}):
	if maximum == None: maximum = n-1
	if (n,maximum) in d:
		return d[(n,maximum)]
	count = 0
	if n <= 1:
		return 0
	if maximum == 1:
		return 1
	# the way to count n = (n-maximum) + maximum
	for p in range(maximum,0,-1):
		if n - p >= 0:
			count += max(numberOfWays(n-p,p,d),1)
	d[(n,maximum)] = count			
	return count

def problem76():
	return numberOfWays(100)

from cProfile import run
if __name__ == "__main__":
	print(problem76() == 190569291)
	run("problem76()")