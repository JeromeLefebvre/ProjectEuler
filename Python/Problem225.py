#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=225
Tribonacci non-divisors
Problem 225
The sequence 1, 1, 1, 3, 5, 9, 17, 31, 57, 105, 193, 355, 653, 1201 ...
is defined by T1 = T2 = T3 = 1 and Tn = Tn-1 + Tn-2 + Tn-3.

It can be shown that 27 does not divide any terms of this sequence.
In fact, 27 is the first odd number with this property.

Find the 124th odd number that does not divide any terms of the above sequence.
'''

'''
Notes on problem 225():
'''
from projectEuler import primes,factorize

def iTribonacci(maximum=10**10):
	T1,T2,T3 = 1,1,1
	yield T1
	yield T2
	yield T3
	Tn = 0
	while Tn < maximum:
		Tn = T1+T2+T3
		yield Tn
		T1,T2,T3 = T2,T3,Tn

def problem225():
	GOAL = 10**9000 #2009
	count = 0
	tribonacci = [a for a in iTribonacci(GOAL)]
	for a in range(1,10**10,2):
		flag = True
		for t in tribonacci:
			if t % a == 0:
				flag = False
				break
		if flag:
			count += 1
		if count == 124:
			return a

if __name__ == "__main__":
	print(problem225())
 