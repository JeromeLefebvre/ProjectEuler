#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=122
Efficient exponentiation
Problem 122
'''

'''
Notes on problem 122():
'''

from itertools import combinations_with_replacement
# Improvements, if 
def problem122():
	records = {k:100 for k in range(1,200+1)}
	def length(k,powers={1,2},history=1):
		if 	history >= records[k]:
			return
		sortedPowers = sorted(list(powers))
		for pair in combinations_with_replacement(sortedPowers[::-1],2):
			s = sum(pair)
			if s == k:
				records[k] = min(records[k], history + 1)
				break
			elif sum(pair) < k:
				length(k, powers.union({s}), history + 1)
			else: #I've over shot
				pass
	total = 1 # accounting for one
	for k in range(2,200+1):
		length(k)
		total += records[k]
		print(k,records[k],total,k**(records[k]-1), k**(records[k]))
	return total

def problem122a():
	foundPowers = {i:set() for i in range(0,201)}
	foundPowers[2] = {2}
	foundPowers[1] = {1}
	foundPowers[0] = {0}
	for i in range(2,200):
		for j in range(i-1,i+1):
			for a in foundPowers[i]:
				for b in foundPowers[j]:
					if a+b in foundPowers[i]: continue
					foundPowers[i+1].add(a+b)
		print(max(foundPowers[i]))		

from cProfile import run
if __name__ == "__main__":
	#run("problem122()")
	print(problem122a()) 