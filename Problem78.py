#!/usr/local/bin/python3.3

'''
Problem 78
Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can separated into piles in exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O
Find the least value of n for which p(n) is divisible by one million.
'''

'''
Notes on problem 78():
'''
from projectEuler import primes

'''
	re the exponents of x on the right hand side are the generalized pentagonal numbers; i.e., numbers of the form ½m(3m − 1), where m is an integer. The signs in the summation alternate as (-1)m. This theorem can be used to derive a recurrence for the partition function:
p(k) = p(k − 1) + p(k − 2) − p(k − 5) − p(k − 7) + p(k − 12) + p(k − 15) − p(k − 22) − ...
'''
def penta(m):
	return m*(3*m-1)//2

def p(n,_d = {0:1}):
	if n < 0:
		return 0
	if n in _d: return _d[n]
	total = 0
	m = 1
	while n - penta(m) >= 0:
		total += (-1)**(m+1) * p(n - penta(m)) + (-1)**(m+1) * p(n - penta(-m))
		m += 1
	_d[n] = total
	return total


def problem78():
	n = 0
	while p(n) % 10**6 != 0:
		n+= 1
	return n


if __name__ == "__main__":
	print(problem78())
