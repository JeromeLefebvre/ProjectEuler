#!/usr/local/bin/python3.3

'''
Problem 63
The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
'''

'''
Notes on problem 63():
'''

def problem63():
	count = 0
	# Find a reason why n is bounded by n
	# or why i is bounded by 100000
	for n in range(1,50):
		for i in range(1,10000):
			if len(str(i**n)) == n:
				#print(n,i**n)
				count += 1
			if len(str(i**n)) > n:
				break
	return count

from cProfile import run
if __name__ == "__main__":
	print(problem63() == 49)
	run("problem63()")
 