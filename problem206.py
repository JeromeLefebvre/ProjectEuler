#!/usr/local/bin/python3.3

'''
Problem 206
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
'''

'''
Notes on problem 206():
'''
from projectEuler import primes

def matches(n):
	for j in range(1,10):
		if n[2*j-2] != str(j):
			return False
	if n[18] != '0':
		return False
	return True

def problem206():
	initial = 1020304050607080900
	initial = 1929374254627488900
	for i in range(int(initial**(1/2))-10, int(2020304050607080900**(1/2))):
		if matches(str(i**2)):
			return i


if __name__ == "__main__":
	print(problem206())
 