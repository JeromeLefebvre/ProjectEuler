#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=103()
Special subset sums: optimum
Problem 103
Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:

S(B) ≠ S(C); that is, sums of subsets cannot be equal.
If B contains more elements than C then S(B) > S(C).
If S(A) is minimised for a given n, we shall call it an optimum special sum set. The first five optimum special sum sets are given below.

n = 1: {1}
n = 2: {1, 2}
n = 3: {2, 3, 4}
n = 4: {3, 5, 6, 7}
n = 5: {6, 9, 11, 12, 13}

It seems that for a given optimum set, A = {a1, a2, ... , an}, the next optimum set is of the form B = {b, a1+b, a2+b, ... ,an+b}, where b is the "middle" element on the previous row.

By applying this "rule" we would expect the optimum set for n = 6 to be A = {11, 17, 20, 22, 23, 24}, with S(A) = 117. However, this is not the optimum set, as we have merely applied an algorithm to provide a near optimum set. The optimum set for n = 6 is A = {11, 18, 19, 20, 22, 25}, with S(A) = 115 and corresponding set string: 111819202225.

Given that A is an optimum special sum set for n = 7, find its set string.

NOTE: This problem is related to problems 105 and 106.
'''

'''
Notes on problem 103():
'''

from random import randint, choice, sample

import itertools
def findsubsets(S,m):
    return set(itertools.combinations(S, m))

def isSpecialSumA(A):
	''' Let's try a MC algo that checks if it is special sum'''
	''' Or else we have to compare 2**7 sets to each other, unless there is a smarter way of doing so'''
	''' DOES NOT WORK WITH SETS OF size 3??'''
	for i in range(1,2000):
		lenB = randint(1,len(A))
		lenC = randint(1,len(A))
		B = sample(A,lenB)
		C = sample(A,lenC)
		if sum(B) == sum(C) and B != C:
			return False
		if lenB > lenC and sum(B) < sum(C):
			return False
		if lenB < lenC and sum(B) > sum(C):
			return False
	return True

import itertools
from itertools import chain, combinations

def powerset(iterable):
  xs = list(iterable)
  # note we return an iterator rather than a list
  return chain.from_iterable( combinations(xs,n) for n in range(len(xs)+1) )

def isSpecialSum(A):
	seenSums = []
	for B,C in combinations(powerset(A),2):
		if sum(B) == sum(C):
			return False
		if len(B) < len(C) and sum(B) > sum(C):
			return False
		if len(B) > len(C) and sum(C) > sum(B):
			return False
	return True

def newSet(A):
	x,y,z = sample(A,1)[0],sample(A,1)[0],sample(A,1)[0]
	if x-1 > 0 and not x - 1 in A:
		A.remove(x)
		A.add(x-1)
	if y != x and not y + 1 in A:
		A.remove(y)
		A.add(y+1)
	if z-1 >0 and y != z and x != z and not z - 1 in A:
		A.remove(z)
		A.add(z-1)

import copy
def problem103():
	A = {21, 11+21, 18+21, 19+21, 21+21, 22+21, 25+21}
	record = sum(A)
	recordSet = A
	maxi = 0
	for i in range(1,1000):
		B = copy.copy(recordSet)
		for j in range(1,20):
			newSet(B)				
			if sum(B) < sum(recordSet) and isSpecialSum(B):
				recordSet = B
				print(B)
				maxi = i
				print(i)
				break
	recordSet = list(recordSet)
	recordSet.sort()
	print(maxi)
	return int(''.join([str(a) for a in recordSet])), sum(recordSet)


if __name__ == "__main__":
	print(problem103() == 20313839404245)
 