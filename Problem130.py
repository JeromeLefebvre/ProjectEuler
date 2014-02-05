#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=130
Composites with prime repunit property
Problem 130
A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k; for example, R(6) = 111111.

Given that n is a positive integer and GCD(n, 10) = 1, it can be shown that there always exists a value, k, for which R(k) is divisible by n, and let A(n) be the least such value of k; for example, A(7) = 6 and A(41) = 5.

You are given that for all primes, p > 5, that p − 1 is divisible by A(p). For example, when p = 41, A(41) = 5, and 40 is divisible by 5.

However, there are rare composite values for which this is also true; the first five examples being 91, 259, 451, 481, and 703.

Find the sum of the first twenty-five composite values of n for which
GCD(n, 10) = 1 and n − 1 is divisible by A(n).
'''

'''
Notes on problem 130():
'''
from projectEuler import primes
from MillerRabin import isPrime
from fractions import gcd
def R(k):
	return int( str(1)*k )

# p -1 % A(p) == 0 for all p > 5
def A(n):
	k = 1
	while True:
		if R(k) % n == 0:
			return k
		k += 1
def problem130():
	count = 0
	n = 1
	total = 0
	while count < 25:
		if gcd(n,10) == 1 and not isPrime(n) and (n-1)%A(n) == 0:
			count += 1
			total += n
		n+=1
	return total




if __name__ == "__main__":
	print(problem130())
 