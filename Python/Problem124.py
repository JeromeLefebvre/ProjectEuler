#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=124()
Ordered radicals
Problem 124
The radical of n, rad(n), is the product of distinct prime factors of n. For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.

If we calculate rad(n) for 1 ≤ n ≤ 10, then sort them on rad(n), and sorting on n if the radical values are equal, we get:

Let E(k) be the kth element in the sorted n column; for example, E(4) = 8 and E(6) = 9.

If rad(n) is sorted for 1 ≤ n ≤ 100000, find E(10000).
'''

'''
Notes on problem 124():
'''
from projectEuler import primes, product, radFromFactors



def problem124():
	checker = primes(save=True,initial=False)
	unsorted = [(1,1)]
	for c in generateFactors(100000,checker):
		unsorted.append((radFromFactors(c),product(c)))
	# Python already sorts list of tuples as first index first, second index in case of ties
	# so we use this by adding the elements rad(n) first
	unsorted.sort()
	return unsorted[10000-1][1]


if __name__ == "__main__":
	print(problem124() == 21417)
 