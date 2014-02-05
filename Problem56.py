
'''
Problem 56
A googol (10100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
'''

from PE_digits import applyToDigits

from itertools import permutations

def problem56():
	return max(applyToDigits(a**b, lambda x: x) for a,b in permutations(range(90,100), 2))

def problem56a():
	record = 0
	# As a and b increase, the number of digits of a**b increase and thus the
	# sum of digits will also likely increase.
	# For example 90**90 has 176 digits, so a number around it should have a digit sum of around 5*176
	# And it keeps increasing from there.
	for a in range(90,100):
		for b in range(90,100):
			# Unsure why, but it appears that in this case
			# String conversion is faster
			s = sum([int(j) for j in str(a**b)])
			if s > record:
				record = s
	return record

from cProfile import run
if __name__ == "__main__":
	print(problem56() == 972)
	run("problem56()")
	print(problem56a() == 972)
	run("problem56a()")

