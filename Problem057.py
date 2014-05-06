#!/usr/local/bin/python3.3

'''
It is possible to show that the square root of two can be expressed as an infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
'''

'''
Notes on problem 57():
'''
from PE_digits import numberOfDigits
from functools import reduce
from fractions import Fraction
def f(a):
	return 1 + 1/(1+a)

def compose(*functions):
    def compose2(f, g):
        return lambda x: f(g(x))
    return reduce(compose2, functions)

def problem57():
	count = 0
	a = Fraction(1)
	for i in range(1,1000):
		a = f(a)
		if len(str(a.denominator)) < len(str(a.numerator)):
			count += 1
	return count

def problem57a():
	count = 0
	a = Fraction(1)
	for i in range(1,1000):
		a = f(a)
		if numberOfDigits(a.denominator) < numberOfDigits(a.numerator):
			count += 1
	return count	
	
from cProfile import run
if __name__ == "__main__":
	print(problem57())
	run("problem57()")
	print(problem57a())
	run("problem57a()")	