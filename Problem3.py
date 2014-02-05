#!/usr/local/bin/python3.3

'''
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

'''
Notes on problem 3():
'''
from PE_primes import factorize

def problem3():
	return max(factorize(600851475143))

import cProfile
if __name__ == "__main__":
	print(problem3() == 6857)
	cProfile.run("problem3()")