#!/usr/local/bin/python3.3

'''
Problem 73
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?
'''

'''
Notes on problem 73():
'''

from fractions import gcd
from pe.basic import product
def relPrimeFromFactors(n,d):
	for p in set(n):
		if p in d:
			return False
	return True

def generateFactors(n,start,checker, factors=[]):
	if start <= n//product(factors):	 
		for a in checker[start:n//product(factors)]:
			yield factors + [a]
			for c in generateFactors(n,a,checker,factors+[a]):
				yield c

def problem73a():
	total = 0
	from factorGenerating import genFactors
	for d in genFactors(12000):
		if d in [(1,)]: continue
		for n in genFactors(product(d)):
			r = product(n)/product(d)
			if relPrimeFromFactors(n,d) == 1 and r > 1/3 and r < 1/2:
				total += 1
	return total

def problem73():
	total = 0
	for d in range(1,1200+1):
		for n in range(d//3-1,d//2+1):
			if gcd(d,n) == 1 and n/d < 1/2 and n/d > 1/3:
				total += 1
	return total

import itertools
def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

def nextGen(tree):
	newTree = []
	for a,b in pairwise(tree):
		newTree.append(a)
		n = a.numerator + b.numerator
		d = a.denominator + b.denominator
		if d <= 60:
			newTree.append( F(n,d) )
	newTree.append(b)
	return newTree

def nextGen(tree):
	for i in range(0,len(tree)):
		a, b = tree[i],tree[i+1]
		n = a.numerator + b.numerator
		d = a.denominator + b.denominator
		newEntry = F(n,d)
		if newEntry.denominator <= 12000:
			tree.insert(i,newEntry)

from fractions import Fraction as F
def problem73b():
	tree = [F(1,3), F(1,2)]
	for i in range(1,20):
		nextGen(tree)
	print(len( tree) - 2)

def nextGen(tree):
	for i in range(0,len(tree)-1):
		a, b = tree[i],tree[i+1]
		d = a + b
		if d <= 100:
			tree.insert(i,d)
			i += 1

from fractions import Fraction as F
def problem73c():
	tree = [3, 2]
	for i in range(1,40):
		nextGen(tree)
	print(len( tree) - 2)

# Think of using: http://keyzero.wordpress.com/2010/04/09/project-euler-problem-73/
# or http://en.wikipedia.org/wiki/Farey_sequence#Next_term
def problem73():
	return sum(1 for d in range(2, 12001) for n in range(d//3, d//2+1) if (n*3 > d) and (n*2 < d) and gcd(n, d) == 1)
from cProfile import run
if __name__ == "__main__":
	print(problem73() == 7295372)
	#print(problem73())# == 7295372)
	run("problem73()")