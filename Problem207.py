#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=207
Integer partition equations
Problem 207
'''

'''
Notes on problem 207():
'''

from itertools import count
from math import log

def P(m):
	countLog = 0
	powersOf2 = [2**i for i in range(1,20)]
	for n in count(3):
		if n in powersOf2: continue
		t = log(n,2)
		if 4**t - 2**t > m:
			break
		countLog += 1

	countInt = 0
	for t in count(1):
		if 4**t - 2**t > m:
			break
		countInt += 1
	return (countInt, countInt+countLog)

def P(m,_d={2,(1,0)}):
	if m not in _d:
		(countInt,countLog) = P(m-1)

		return 
def problem207():
	for n in count(147630):
		a,b = P(n)
		if a/b < 1/1234:
			return n
	

#Implement this: https://wiki.python.org/moin/PythonDecoratorLibrary#Memoize

from cProfile import run
if __name__ == "__main__":
	#run("problem207()")
	print(problem207()) 