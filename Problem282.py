#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=282
The Ackermann function
Problem 282
For non-negative integers m, n, the Ackermann function A(m, n) is defined as follows:


For example A(1, 0) = 2, A(2, 2) = 7 and A(3, 4) = 125.

Find A(n, n) and give your answer mod 148.
'''

'''
Notes on problem 282():
'''


def modularPow(x, y, z):
	"Calculate (x ** y) % z efficiently."
	number = 1
	while y:
		if y & 1:
			number = number * x % z
		y >>= 1
		x = x * x % z
	return number

def f(n): return (16*pow(2,n-1,14**8) - 3)% 14**8

def A(m,n,_d = {(1,0): 2,(4,0):13}):
	#print(m,n)
	if (m,n) in _d: return _d[(m,n)]
	if m == 0:
		_d[(m,n)] = (n+1) % 14**8
	elif m == 1:
		_d[(m,n)] = n+2 % 14**8
	elif m == 2:
		_d[(m,n)] = (2*n + 3) % 14**8
	elif m == 3:
		# We have the recurence relation f(n) = 2f(n-1) + 3
		# Which we can solve as follows:
		#def f(n): return int((10+6)*2**(n-1) - 3)% 14**8
		_d[(m,n)] = f(n) % 14**8
	elif m == 4:
		_d[(m,n)] = f(A(m,n-1)) % 14**8
	elif m > 4 and n == 0:
		_d[(m,n)] = A(m-1,1) % 14**8
	elif m > 0 and n > 0:
		_d[(m,n)] = A(m-1,A(m,n-1)) % 14**8
	return _d[(m,n)]

import sys
sys.setrecursionlimit(5000)
def problem282():
	print(A(1,1))
	print(A(2,2))
	print(A(3,3))
	print(A(4,4))
	print(A(4,1000))
	print(A(5,1))
	



if __name__ == "__main__":
	print(problem282() == 982905341)
 