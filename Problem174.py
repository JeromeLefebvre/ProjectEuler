#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=174
Counting the number of "hollow" square laminae that can form one, two, three, ... distinct arrangements
Problem 174
'''

'''
Notes on problem 174():
'''

from collections import defaultdict

def problem174():
	found = defaultdict(int)
	GOAL = 10**6
	for w in range(1,2*GOAL):
		for l in range(1,2*GOAL//(4*w) + 1):
			if 4*(w**2 + w*l) <= GOAL:
				found[4*(w**2 + w*l)] += 1
	count = 0
	for r in range(1,10**6):
		if 1 <= found[r] <= 10:
			count += 1
	return count


from cProfile import run
if __name__ == "__main__":
	#run("problem174()")
	print(problem174()) 