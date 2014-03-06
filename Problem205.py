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
from random import randint
from collections import defaultdict

def sums(maxPips, numberOfDices):
	sums = defaultdict(int)
	def waysToSumTo(dicesLeft=numberOfDices, soFar=0):
		if dicesLeft == 0:
			sums[soFar] += 1
		else:
			for pip in range(1,maxPips+1):
				waysToSumTo(dicesLeft-1, soFar + pip)
	waysToSumTo()
	return sums

def problem205():
	peter = sums(4,9)
	colin = sums(6,6)
	totalGames = (4**9) * (6**6)
	wins = 0
	for C in range(0, 36+1):
	    for P in range (C+1, 36+1):
	        wins += peter[P]*colin[C]
	return round(wins/totalGames,7)


if __name__ == "__main__":
	print(problem205() == 0.5731441)
 