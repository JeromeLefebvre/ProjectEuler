
'''
Factorial digit sum
Problem 20
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''
from math import factorial
from PE_digits import applyToDigits

# Too easy in python
def problem20():
	return applyToDigits(factorial(100))

from cProfile import run
if __name__ == "__main__":
	print(problem20() == 648)
	run("problem20()")
