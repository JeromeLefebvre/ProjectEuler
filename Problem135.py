#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=135
Same differences
Problem 135

'''

'''
Notes on problem 135():
'''

from collections import defaultdict

from itertools import count

def problem135():
	seen = 0
	found = defaultdict(int)
	for l in count(1):
		for x in count(1):
			n = 2*l*x + 3*l**2 - x**2
			if n >= 10**6: continue
			if n <= 0: break
			found[n] += 1
			if found[n] == 10:
				seen += 1
				print(l,seen)
			if found[n] == 11:
				seen -= 1

def problem135():
	found = defaultdict(int)
	for u in range(1,10**6+1):
		for v in count(1):
			if u*v > 10**6: break
			if (u + v) % 4 == 0 and 3*v > u and (3*v - u) % 4 == 0:
				found[u*v] += 1
	return sum( 1 for key in found if found[key] == 10)

def problem135():
	found = defaultdict(int)
	for u in range(1,10**6+1):
		for v in range(u//3+1, 10**6 // u + 1):
			if (u + v) % 4 == 0 and (3*v - u) % 4 == 0:
				found[u*v] += 1
	return sum( 1 for key in found if found[key] == 10)

from cProfile import run
if __name__ == "__main__":
	#run("problem135()")
	print(problem135())# == 4989)