#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=303
Multiples with small digits
Problem 303
'''

'''
Notes on problem 303():
'''

def isMadeOf2(n):
	return set(str(n)) <= {'0','1','2'}

from itertools import count

def g(n):
	k = 1
	m = n
	while not isMadeOf2(m):
		m += n
		k += 1
	return m #//n

from PE_primes import factorize
from PE_basic import gcdd

def problem303():
	numbers99 = [i for i in range(999,10000,999)]
	n = 999
	f = {}
	#print(g(2*9))
	#print(g(2*99))
	return factorize(1111222222222222222222)

	while len(numbers99) != 0:
		if isMadeOf2(n):
			numbersToRemove = []
			for k in numbers99:
				if n % k == 0:
					print(k)
					numbersToRemove.append(k)
					f[k] = n
			if len(numbersToRemove) != 0:
				print(factorize(n))
				print(gcdd(*numbers99))
			for number in numbersToRemove:
				numbers99.remove(number)
		n += 999
	print(f)
	#return sum( f(n) for n in range(1,101))

def numberFromList(c):
	total = 0
	for index, digit in enumerate(c):
		total += digit*10**(len(c)-index - 1)
	return total

from itertools import product

def problem303a():
	GOAL = 10000
	numbers = [i for i in range(1,GOAL+1)]
	total = 0
	f = {}
	total = 0
	f[999] = 111222222222222//999
	numbers.remove(999)
	f[2*999] = 111222222222222//(2*999)
	f[9999] = 11112222222222222222 // 9999
	numbers.remove(9999)
	for numberOfDigits in count(0):
		print(numberOfDigits, len(numbers), gcdd(*numbers))
		if len(numbers) <= 15:
			print(numbers)
		for c in product( *([[1,2]] + [[0,1,2]]*numberOfDigits)):
			m = numberFromList(c)
			numbersToRemove = []
			for number in numbers:
				if m % number == 0:
					f[number] = m // number
					numbersToRemove.append(number)
			for number in numbersToRemove:
				numbers.remove(number)
			if len(numbers) == 0:
				#for n in range(1,GOAL+1):
				#	if f[n] != g(n): print("************",n, f[n],g(n))
				return sum( f[n] for n in range(1,GOAL+1))


from cProfile import run
if __name__ == "__main__":
	#run("problem303()")
	print(problem303a())# == 11363107) 