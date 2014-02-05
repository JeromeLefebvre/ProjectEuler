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


	


from cProfile import run
if __name__ == "__main__":
	run("problem()")
 
 