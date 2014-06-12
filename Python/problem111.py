#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=111
Primes with runs
Problem 111
'''

'''
Notes on problem 111():
'''

from itertools import dropwhile
from PE_primes import iPrime

def problem111(GOAL):
	M = [0]*10
	N = [[],[],[],[],[],[],[],[],[],[]]
	for p in dropwhile(lambda x: x<10**GOAL, iPrime()):
		if p > 10**(GOAL + 1): break
		sp = str(p)
		for i in range(0,10):
			if sp.count(str(i)) > M[i]:
				M[i] = sp.count(str(i))
				N[i] = []
			if sp.count(str(i)) == M[i]:
				N[i].append(p)
	for i in range(len(N)):
		print(i, M[i], sum(N[i]))

from PE_primes import isPrime
from itertools import combinations
import itertools
def problem111a():
	# 9 digits the same
	# 1 digit is the same
	
	total = 0
	for digits in [str(i) for i in range(0,10)]:
		count = 0
		for index in range(0,10):
			for a in range(0,10):
				number = [digits]*9
				number.insert(index,str(a))
				a = int(''.join(number))
				if len(str(a)) == 10 and isPrime(a):
					total += a
					#print(a)
	
	for digits in ['2','8','0']:
		count = 0
		for index1,index2 in combinations([i for i in range(0,10)],2):
			for a,b in itertools.product(range(10),range(10)):
				number = [digits]*10
				number[index1] = str(a)
				number[index2] = str(b)
				a = int(''.join(number))
				if len(str(a)) == 10 and isPrime(a):
					total += a
	return total

from cProfile import run
if __name__ == "__main__":
	#run("problem111a()")
	print(problem111a())