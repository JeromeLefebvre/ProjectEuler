


#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=235()
An Arithmetic Geometric sequence
Problem 235
Given is the arithmetic-geometric sequence u(k) = (900-3k)rk-1.
Let s(n) = Σk=1...nu(k).

Find the value of r for which s(5000) = -600,000,000,000.

Give your answer rounded to 12 places behind the decimal point.
'''

'''
Notes on problem 235():
There is a way to actually write a closed form formula for S(n).
But, python is quick enough that this is not needed.
The output is tricky, with prec = 13, we get 12 decimals
but it is rounded down. So, the output should be raised by one.

'''


from decimal import *

def problem235():
	def f(k,r): return (900 - 3*k)*r**(k-1)
	def sumDumb(n,r):
		return sum([f(k,r) for k in range(1,n+1)])

	
	getcontext().prec = 14

	high = Decimal(1.2)
	low = Decimal(1)
	guess = low + (high - low)/2
	for i in range(1,400):
		if sumDumb(5000,guess) + Decimal(600000000000) > 0:
			low = guess
		else:
			high = guess
		guess = low + (high - low)/2
	return guess



if __name__ == "__main__":
	print(problem235())
 



#1.0023221086328761428 -599999999999.99995366
#1.0023221086328761428 -599999999999.99995366
#1.00232210863287614281680609076 -599999999999.999999999999996525