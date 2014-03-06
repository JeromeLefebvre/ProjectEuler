#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=146
Investigating a Prime Pattern
Problem 146
'''

'''
Notes on problem 146():
'''
from PE_primes import isPrime, primesUpTo

'''10
315410
927070
2525870
8146100
16755190
39313460'''
def problem146():
	total = 0
	# n % 210 = 10
	for n in range(10,15*10**7,210):
		if all([isPrime(n**2 + i) for i in [1,3,7,9,13,27]]):
			print(n)
			total += n
	# n % 210 = 80
	for n in range(80,15*10**7,210):
		if all([isPrime(n**2 + i) for i in [1,3,7,9,13,27]]):
			print(n)
			total += n
	# n % 210 = 130	
	for n in range(130,15*10**7,210):
		if all([isPrime(n**2 + i) for i in [1,3,7,9,13,27]]):
			print(n)
			total += n
	# n % 210 = 200
	for n in range(200,15*10**7,210):
		if all([isPrime(n**2 + i) for i in [1,3,7,9,13,27]]):
			print(n)
			total += n			
	return total

if __name__ == "__main__":
	print(problem146())
 