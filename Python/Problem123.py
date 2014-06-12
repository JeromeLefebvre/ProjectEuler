#!/usr/local/bin/python3.3

'''
Prime square remainders
Problem 123
Let pn be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder when (pn−1)n + (pn+1)n is divided by pn2.

For example, when n = 3, p3 = 5, and 43 + 63 = 280 ≡ 5 mod 25.

The least value of n for which the remainder first exceeds 109 is 7037.

Find the least value of n for which the remainder first exceeds 1010.
'''

'''
Notes on problem 123():
'''
from projectEuler import primes

def problem123():
	checker = primes(save=True,initial=False)
	for n, p in enumerate(checker[0:10**6]):
		#print(n+1,p)
		if (n+1) % 2 == 1 and 2*(n+1)*p > 10**10:
			return n + 1

if __name__ == "__main__":
	print(problem123())
 