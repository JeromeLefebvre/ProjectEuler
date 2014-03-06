#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=160
Factorial trailing digits
Problem 160
'''

'''
Notes on problem 160():
'''

def modularFactorial(n,mod=10**5):
	fact = 1
	while n > 0:
		fact *= n
		while fact >0 and fact % 10 == 0:
			fact //= 10
		fact %= mod
		n -= 1
	return fact % mod

def modularFactorial(n,mod=10**5):
	fact = 1
	while n > 0:
		m = n 
		while m % 10 == 0:
			m //= 10
		fact *= m
		while fact >0 and fact % 10 == 0:
			fact //= 10
		fact %= mod
		n -= 1
	return fact % mod

'''
>>> modularFactorial(10**5)
62496
>>> modularFactorial(10**6)
88544
>>> modularFactorial(10**7)
56448
f(100)=16864
'''

from math import log
def factorsOf2(n):
	l = int(log(n,2))
	total = 0
	for power in range(1,l+1):
		total += n//(2**power)
	return total

def factorsOf5(n):
	l = int(log(n,5))
	total = 0
	for power in range(1,l+1):
		total += n//(5**power)
	return total


from math import factorial
def factorsOf22(n):
	l = 0
	n = factorial(n)
	while n % 2 == 0:
		l += 1
		n //= 2
	return l

def problem160():
	d = {}
	for n in range(1,10**4):
		fn = modularFactorial(n)
		if fn not in d:
			d[fn] = [n]
		else:
			d[fn].append(n)
	for key in d:
		if len(d[key]) > 3:
			print(key,d[key])

'''
1 1
1 2
2 3
6 4
5
24 5
120 6
720 7
5040 8
40320 9
362880
'''
def problem160():
	n = 1
	check = True
	for i in range(1,10**7):
		n *= i
		while n % 10 == 0:
			n //= 10
		n %= 10**5
	return n
	return factorsOf5(10**12), factorial(24)

	


from cProfile import run
if __name__ == "__main__":
	#run("problem160()")
 	print(problem160())
 