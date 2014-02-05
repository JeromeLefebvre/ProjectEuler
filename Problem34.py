
'''
Problem 34
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

'''

def digits(m):
	M = []
	while m > 0:
		M.append(m%10)
		m //= 10
	return M

def problem34():
	''' This is a digit problem so we approach it this way'''
	from itertools import combinations_with_replacement
	from math import factorial
	total = 0
	for n in range(2,6):
		for c in combinations_with_replacement(range(0,10),n):
			m = sum([factorial(i) for i in c])
			if sorted(digits(m)) == list(c):
				total += m
	return total

def problem34a():
	from math import factorial
	from PE_digits import applyToDigits
	total = 0
	# Being lazy
	for i in range(3,100000):
		if i == sum([factorial(int(a)) for a in str(i)]):
			total += i
	return total

from cProfile import run
if __name__ == "__main__":
	print(problem34() == 40730)
	run("problem34()")
	print(problem34a() == 40730)
	run("problem34a()")	
 
