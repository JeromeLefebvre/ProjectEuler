#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=121
Disc game prize fund
Problem 121
'''

'''
Notes on problem 121():
'''

from itertools import combinations
from fractions import Fraction as F

from PE_basic import product

def problem121():
	n = 4
	oldlevel = [1]
	for i in range(1,16):
		newlevel = [1]
		for j in range(0,len(oldlevel)-1):
			newlevel.append(i*oldlevel[j] + oldlevel[j+1])
		newlevel.append(i*oldlevel[-1])
		#print(i,newlevel)
		oldlevel = newlevel

	l = 1/F( sum(newlevel[u] for u in range(0,8)) , sum(newlevel))
	return int(l)
	

from cProfile import run
if __name__ == "__main__":
	#run("problem121()")
	print(problem121()) 