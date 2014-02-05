#!/usr/local/bin/python3.3



def finiteGeometricSum(r,n):
	''' Returns \sum_{k=0}^{n-1} r^k = r^0 + r^1 + \cdots + r^{n-1}
	Warning: This suffers from a loss in precision, for example: 
	>>> finiteGeometricSum(1/2,60)
	2.0'''
	return (1 - r**n)/(1-r)

from functools import reduce
from operator import mul
import itertools


################################################################
############ Various special values
################################################################

################################################################
############ Various sequences
################################################################



def Fib(n):
	''' This is the sequence where >>> Fib(0)
0
>>> Fib(1)
1
>>> Fib(2)
1
>>> Fib(3)
2'''
	return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))

from MillerRabin import isPrime
from random import randint
from fractions import gcd


def isSquareA(n):
	''' A pure integer solution of isSquare'''
	if n in [0,1]:
		return True
	x = n // 2
	seen = set([x])
	while x**2 != n:
		# Here we take the average between x and n//x and this becomes out new x
		# with this, at every step x and n//x both approach the square root of n
		x = (x + n // x) // 2
		# If x shows up twice, then x dipped below the square root and taking the average
		# will increase x back up or leave it as is, either case we have failed.
		if x in seen: return False
		seen.add(x)
	return True

def isSquare(n):
	''' Returns True if the integer n is a square in the integers'''
	# This is a much faster version of isSquare
	return int(n**(1/2))**2 == n

def isPandigital(n):
	return set(str(n)) == {str(i) for i in range(1,len(str(n))+1)} and n < 10**10



#####################################################
##### isFunctions
####################################################
def isPalindrome(n):
	'''Returns True if a number is a palindrome'''
	return str(n) == str(n)[::-1]



def isAnagram(word,word2):
	if set(word) != set(word2):
		return False
	for a in set(word):
		if word.count(a) != word2.count(a):
			return False
	return True

def isLychrel(n):
	n = n + int(str(n)[::-1])
	for i in range(1,50):
		if isPalindrome(n):
			return False
		n = n + int(str(n)[::-1])
	return True

def isTriangle(a):
	''' I.e. is there a solutin to a = n*(n+1)/2 in the positive integers?'''
	return any(n >= 0 for n in solveIntegerQuadratic(1,1,-2*a))

def isPentagonal(a):
	return any(n > 0 for n in solveIntegerQuadratic(3,-1,-2*a))

def isHexagonal(a):
	return any(n > 0 for n in solveIntegerQuadratic(2,-1,-a))

def isDigit(n):
	return all(str(n).count(a) == 1 for a in set(str(n)))

def isMadeOfOdd(n):
	return set(str(n)) <= {'1','3','5','7','9'}

#####################################################
# Functions dealing with collatz sequence
########################################	
def collatz(n):
	''' A basic interator that generates the terms of the collatz sequence'''
	while n > 1:
		yield n
		if n % 2 == 0:
			n = n / 2			
		else:
			n = 3*n + 1			
	yield 1




##################################################
### Dealing with factors directly
##################################################

def numberFactory(bases=[2, 3, 5, 7, 11,13,17],n=100000):
	nums = [1] * n
	candidates_indexes = [0 for _ in bases]
	candidates = [base for base in bases]
	for i in range(1, n):
		nextn = min(candidates)
		nums[i] = nextn
		yield nextn
		for index, val in enumerate(candidates):
			if val == nextn:
				candidates_indexes[index] += 1
				candidates[index] = bases[index] * nums[candidates_indexes[index]]


def numberFactory2(bases=[2, 3, 5, 7, 11,13,17],n=100000):
	nums = [1]* n
	factors = [[]]*n
	candidates_indexes = [0 for _ in bases]
	candidates = [base for base in bases]
	for i in range(1, n):
		nextn = min(candidates)
		nums[i] = nextn
		yield nextn, factors[i]
		for index, val in enumerate(candidates):
			if val == nextn:
				candidates_indexes[index] += 1
				candidates[index] = bases[index] * nums[candidates_indexes[index]]
				factors[index].append([bases[index]] * nums[candidates_indexes[index]])


def isAbudantFromFactors(factors):
	div = divisorsFromFactors(factors)
	return (sum(div) - max(div)) > product(factors)

def isAbudant(n):
	div = divisors(n)
	div.remove(n)
	return sum(div) > n




def generateFactors(n,checker,start=1,factors=[], genOne=False):
	'''This generates all numbers between from 2 up to n as their list of factors'''
	if genOne:
		yield [1]
	if start <= n//product(factors):
		# The -1 is to make sure 2 is included when we are at 3
		for a in checker[start-1:n//product(factors)]:
			yield factors + [a]
			for c in generateFactors(n,checker,a,factors+[a]):
				yield c



def phiFromFactors(factors):
	if factors == []: return 0
	ph = 1
	for p in set(factors):
		ph *= p**factors.count(p) - p**(factors.count(p) - 1)
	return ph

def sigmaFromFactors(factors):
	if factors == []: return 1
	return product([factors.count(p) + 1 for p in set(factors)])

##########################################################################################
### Dealing with integers
##########################################################################################

from math import sqrt

def integerSquare(d):
	''' Expects a square integer '''
	# For some reason, using a power is much faster than calling math.sqrt
	s = int(d**(1/2))
	if d == s**2:
		return s
	# Does this ever fail?civ
	print("INTEGER SQUARE WAS NEEDED")
	return s+1

def solveIntegerLinear(a,b):
	'''Returns all integer solutions to ax + b = 0'''
	# all integers are solutions to 0x = 0
	# so there is no good outputs to this
	if a == 0 and b == 0:
		raise IndexError
	if -b % a == 0:
		return [-b//a]
	return []

def solveIntegerQuadratic(a,b,c):
	''' Returns a list (sorted by size) of all possible integer roots to a quadratic equation of the form ax**2 + bx = c'''

	if a == 0:
		return solveIntegerLinear(b,c)
	disc = b**2 - 4*a*c # The usual discriminant
	# I wish I could return a set, since solutions have no natural order. But it was hard to write up the code using sets
	soln = []
	# We need to make sure that the discriminant is positive and if it is
	# that it is the square of an integer
	if disc >= 0 and isSquare(disc):
		d = int(disc**(1/2))
		# The two possible solutions
		if (-b - d) % (2*a) == 0:
			soln.append((-b - d) // (2*a))
		if (-b + d) % (2*a) == 0:
			soln.append((-b + d) // (2*a))
	soln.sort()
	return soln



##########################################################################################
### Dealing wth digits
##########################################################################################




def numberFromList(l):
	return sum([a*10**index for index,a in enumerate(l)])

def radFromFactors(l):
	return product(set(l))
	
from math import log

from functools import reduce




	
