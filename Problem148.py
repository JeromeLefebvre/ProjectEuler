#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=148
Exploring Pascal's triangle.
Problem 148
We can easily verify that none of the entries in the first seven rows of Pascal's triangle are divisible by 7:

 	 	 	 	 	 	 1
 	 	 	 	 	 1	 	 1
 	 	 	 	 1	 	 2	 	 1
 	 	 	 1	 	 3	 	 3	 	 1
 	 	 1	 	 4	 	 6	 	 4	 	 1
 	 1	 	 5	 	10	 	10	 	 5	 	 1
1	 	 6	 	15	 	20	 	15	 	 6	 	 1
However, if we check the first one hundred rows, we will find that only 2361 of the 5050 entries are not divisible by 7.

Find the number of entries which are not divisible by 7 in the first one billion (109) rows of Pascal's triangle.
'''

'''
Notes on problem 148():
'''
from projectEuler import product, nCk

def base7(n):
	base = []
	while n != 0:
		a = n % 7
		base.append(a)
		n //= 7
	base.reverse()
	return base

def divisible7(n):
	base = base7(n)
	return product( 6 - a for a in base[1:] )

def problem148():
	n = 2*7**2 + 3*7 + 5
	print(divisible7(n))
	total = 0
	for k in range(0,n+1):
		if nCk(n,k) % 7 == 0:
			print(k, base7(k))
	return
	for n in range(1,101):
		total += solutions(n)
	return total



if __name__ == "__main__":
	print(problem148())
 