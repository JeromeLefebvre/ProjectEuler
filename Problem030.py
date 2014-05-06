
'''
Problem30

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''
def problem30():
		"This problem is really a digit problem, so it is much faster to solved it this way"
		from itertools import combinations_with_replacement, chain
		total = 0
		for digits in chain.from_iterable(combinations_with_replacement(range(10),i) for i in range(2,7)):
				a = 0
				for d in digits:
						a += d**5
				s = str(a)
				if len(digits)==len(s) and all(s.count(str(i))==digits.count(i) for i in set(digits)):
						total += a
		return total   

def problem30a():
		# we have this upper bound since 9**5 = 59049
		from PE_digits import applyToDigits
		def f(a): return a**5
		return sum([i for i in range(40,6*9**5) if i == applyToDigits(i,f)])

# Creating the list is just as fast
def problem30b():
		# we have this upper bound since 9**5 = 59049
		from PE_digits import applyToDigits
		def f(a): return a**5
		total = 0
		for i in range(40,6*9**5):
				if i == applyToDigits(i,f):
						total += i
		return total

if __name__ == "__main__":
		from cProfile import run
		print(problem30() == 443839)
		run("problem30()")
		print(problem30a() == 443839)
		run("problem30a()")
		print(problem30b() == 443839)
		run("problem30b()")
