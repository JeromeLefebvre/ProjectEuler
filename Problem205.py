#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=205
Dice Game
Problem 205
Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the form 0.abcdefg
'''

'''
Notes on problem 205():
'''
from projectEuler import primes
from random import randint

def problem205():
	wins = 0
	for n in range(1,10**6):
		p = sum( [ randint(1,4) for i in range(1,10) ] )
		c = sum( [ randint(1,6) for i in range(1,7) ] )
		if p > c:
			wins += 1
	print(wins/n)


if __name__ == "__main__":
	print(problem205())
 