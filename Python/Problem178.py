'''
http://projecteuler.net/problem=178
Step Numbers
Problem 178
'''

'''
Notes on problem 178():
By far one of the fatest solution I was able to find for a problem in the 100.
Around 30mins.
'''

from functools import lru_cache

def problem178():
	@lru_cache(maxsize=4000)
	def seek(current, digitsSeenSofar, maxdepth, depth=1):
		if depth == maxdepth:
			if set(digitsSeenSofar) == {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}:
				return 1
			else:
				return 0
		total = 0
		if current > 0:
			total += seek(current - 1, tuple( set(digitsSeenSofar) | {current-1} ), maxdepth, depth+1)
		if current < 9:
			total += seek(current + 1, tuple( set(digitsSeenSofar) |{current + 1} ), maxdepth, depth+1)
		return total

	total = 0
	for maxdepth in range(10,40+1):
		total += sum([ seek(i, (i,),maxdepth) for i in range(1,10)])
	return total

from cProfile import run
if __name__ == "__main__":
	#run("problem178()")
	print(problem178()) 
