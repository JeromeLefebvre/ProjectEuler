#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=133
Repunit nonfactors
Problem 133
'''

'''
Notes on problem 133():
'''
def A(n):
	#assert(gcd(n,10) == 1)
	o = pow(10,1,9*n)
	count = 1
	while not (o == 1):
		o = pow(o*10,1,9*n)
		count += 1
	return count 


def multipleOf2and5(n):
	while n % 2 == 0 and n != 0:
		n //= 2
	while n % 5 == 0 and n != 0:
		n //= 5
	return n == 1

from PE_primes import iPrime
from itertools import dropwhile

def order(a,n):
	'''Expects (a,n) = 1, returns min k such that a^k = 1 mod n'''
	b = a
	k = 1
	while b % n != 1:
		b *= a
		k += 1
	return k

# [Finished in 15722.4s]  record bad solutions.
def problem133():
	total = 2 + 3 + 5
	for p in dropwhile(lambda x: x < 6, iPrime()):
		if p > 10**5: break
		#print(p, order(10,p))
		if not multipleOf2and5(order(10,p)):			
			total += p
			print(p)
	return total

from cProfile import run
if __name__ == "__main__":
	#run("problem133()")
	print(problem133()) 