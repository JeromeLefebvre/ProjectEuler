
'''
Problem 25

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
'''

from math import log

from pe.sequences import phi


def problem25():
	''' we have our usual bound on Fib()
Which says that phi^n/5**(1/2) = Fib(n)
Thus, we only need to look at = (999log(10) + log(√5))/log(phi)
'''
	n = int((999*log(10) + 1/2*log(5))/log(phi)) + 1
	return n


if __name__ == "__main__":
	print(problem25() == 4782)
	from cProfile import run
	run("problem25()")
