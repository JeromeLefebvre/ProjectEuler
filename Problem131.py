#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=131
Prime cube partnership
Problem 131
'''

'''
Notes on problem 131():
'''
from projectEuler import *
from itertools import count
from MillerRabin import isPrime
from SolvingQuadratics import isSquare
from itertools import combinations
def iCube(maximum=10**10):
	for n in count():
		yield n**3
from factorGenerating import genFactors

def squaresFromDivisors(div):
	return [d for d in div if isSquare(d)]

'''7 0 2
19 1 12
37 2 36
61 3 80
127 4 252
271 5 810
331 6 1100
397 7 1452
547 8 2366
631 9 2940
919 10 5202
1657 11 12696
1801 12 14400
1951 13 16250
2269 14 20412
2437 15 22736
2791 16 27900
3169 17 33792
3571 18 40460'''
def problem131():
	count = 0
	primes = set()
	for a in range(1,10**10):
		for n in range(1,a+1):
			if 0 < (a**3 - n**3) / n**2 < 10**6 and (a**3 - n**3) % n**2 == 0 and isPrime((a**3 - n**3) // n**2):
				count += 1
				print((a**3 - n**3) // n**2, len(primes), a,n)
				primes.add((a**3 - n**3) // n**2)
				break

from projectEuler import factorize
def problem131a():
	count = 0
	for a in range(1,10**5):
		a3 = a**3
		factorsOfa = factorize(a)
		div = divisorsFromFactors( factorsOfa + factorsOfa + factorsOfa )
		for k in div:
			n = isSquare(a3 // k)
			if n and k-n >0 and isPrime(k - n):
				print(k-n)

if __name__ == "__main__":
	print(problem131())
 