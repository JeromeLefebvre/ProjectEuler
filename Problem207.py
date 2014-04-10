#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=207
Integer partition equations
Problem 207
'''

'''
Notes on problem 207():
'''

from itertools import count
from math import log
from memoize import memoize
@memoize
def P(m):
	countLog = 0
	powersOf2 = [2**i for i in range(1,20)]
	for n in count(3):
		if n in powersOf2: continue
		t = log(n,2)
		if 4**t - 2**t > m:
			break
		countLog += 1

	countInt = 0
	for t in count(1):
		if 4**t - 2**t > m:
			break
		countInt += 1
	return (countInt, countInt+countLog)


def problem207():
	for n in count(147630):
		a,b = P(n)
		if n in [5,10,15,20,25,30,180,185]:
			print(n,P(n))
		if a/b < 1/1234:
			return n
	

#Implement this: https://wiki.python.org/moin/PythonDecoratorLibrary#Memoize

from decimal import *
def f(k):
	radical = Decimal(1) + Decimal(4)*k
	radical = Decimal(1) + radical.sqrt()
	logant /= Decimal(2)
	return a.ln()/Decimal(2).ln()

def problem207():
	perfect = 0
	notperfect = 0
	getcontext().prec = 10
	k = Decimal(1)
	while True:
		k += 1
		if k> 30:
			break
		t = f(k)
		print(2**t)
		if int(2**t) == 2**t:
			if int(t) == t:
				perfect += 1
			else:
				notperfect += 1
		print(k, perfect / (perfect+notperfect))

'''
Implement using this!
>>> a.ln()/Decimal(2).ln()
Decimal('3.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001')
>>> b = a.ln()/Decimal(2).ln()
>>> b
Decimal('3.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001')
>>> b.quantize(10)
Decimal('3')
>>> b.quantize(10) == Decimal(3)
True
'''

from cProfile import run
if __name__ == "__main__":
	#run("problem207()")
	print(problem207()) 