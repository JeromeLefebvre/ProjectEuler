#!/usr/local/bin/python3.3

'''
Problem 112
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
'''

'''
Notes on problem 112():
'''
from projectEuler import primes

def isBouncy(n):
	n = str(n)
	increasing = all(n[i] <= n[i+1] for i in range(0,len(n)-1))
	decreasing = all(n[i] >= n[i+1] for i in range(0,len(n)-1))
	return not (increasing or decreasing)

def problem112():
	bouncy = 0
	for i in range(1,10**7+1):
		if isBouncy(i): bouncy += 1
		if bouncy/i == 0.99:
			return i

if __name__ == "__main__":
	print(problem112())
 