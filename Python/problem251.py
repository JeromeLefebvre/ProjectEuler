
# python3.3 -m cProfile problem251.py
'''
10 1
20 2
30 2
40 4
50 6
100 11
200 29
300 40
500 74
1000 149
2000 310
10000 1632
20000 3312
100000 16916
500000 85365
10000000 1719481
Goal:
110000000 18946051

Version 1: n = 200 1293706 function calls in 1.993 seconds
Version 2: n = 200 431218 function calls in 0.668 seconds

Version 3: n = 200 36 function calls in 0.009 seconds
Version 3: n = 2000 5 function calls in 0.967 second
Version 3: n = 10000 5 function calls in 23.380 seconds
Version 3: n = 20000 3319 function calls in 92.755 seconds

Version 4: n = 2000 669 function calls in 0.553 seconds
Version 4: n = 10000 3335 function calls in 14.952 seconds
Version 4: n = 20000 6669 function calls in 63.195 seconds

version 5: n = 20000 229899 function calls (229494 primitive calls) in 1.136 seconds
version 5: n = 100000 1266589 function calls (1266184 primitive calls) in 13.067 seconds
with twist to primeGeneration: 
version 5: n = 100000 1266601 function calls (1266196 primitive calls) in 2.132 seconds
version 5: n = 1000000 14944048 function calls (14943643 primitive calls) in 29.258 seconds
version 5: n = 10000000 173027884 function calls (173027479 primitive calls) in 428.888 seconds
'''

def generator251v2(n):
	for l in range(1,int( (n + 1)/3)):
		a = 3*l - 1
		for b in range(1,n-a):
			for c in range(1,n-a-b):
				yield a,b,c

def generator251v3(n):
	count = 0
	for l in range(1,int( (n + 1)/3)):
		a = 3*l - 1
		for b in range(1,n-a):
			if (((1-2*a)**3)/27 - a**2 )% (b**2) == 0:
				c = int(((1-2*a)**3/(3**3)) - a**2)/(-(b**2))
				if a + b + c <= n:
					count += 1
	return count

def generator251v4(n):
	count = 0
	for l in range(1,int((n + 1)/6) + 1):
		a = 3*l - 1
		bMin = max(int(l*(8*l-3)**(1/2) / (n-a)),1)
		bMax = min(int(l*(8*l - 3)**(1/2)), n-a)
		for b in range(bMin,bMax):
			if (8*l**3 - 3*l**2) % b**2 == 0:
				c = (8*l**3 - 3*l**2) / b**2
				if a + b + c <= n:
					count += 1
	return count

import Brent

def possibleFactorsForb(l):
	# build a list of all possible factors of b
	factors = primeFactors(8*l**3 - 3*l**2)
	for p in set(factors):
			count = factors.count(p)
			while count > 1:
				factorsOfb.append(p**count)
				count -= 2

	return factors


from operator import mul
from functools import reduce
from copy import copy

def multiply(list):
	return reduce(mul, list, 1)


def cube(l):
	prod = multiply([a + 1 for a in l])
	# The origin
	b = [0]*len(l)
	latticePoints = [copy(b)]
	for i in range(1,prod):
		# b + 1
		b[0] += 1
		# we do the carry over
		for j in range(0,len(l)):
			if b[j] == l[j] + 1:
				b[j] = 0
				b[j+1] += 1
		latticePoints.append(copy(b))
	return latticePoints

from Brent import primeFactors

def generator251v5(n):
	count = 0
	for l in range(1,int((n + 1)/6) + 1):
		a = 3*l - 1
		# Need all the prime factors of l**2(8*l - 3)
		factors = primeFactors(l)
		factors += factors
		factors += primeFactors(8*l-3)

		factorsOfb = [0]*len(set(factors))
		listOfPrimes = [0]*len(set(factors))
		for index,p in enumerate(set(factors)):
			factorsOfb[index] = factors.count(p)//2
			listOfPrimes[index] = p

		latticeCube = cube(factorsOfb)
		for vector in latticeCube:			
			b = 1
			for index, p in enumerate(listOfPrimes):
				b *= p**vector[index]

			c = (8*l**3 - 3*l**2) / b**2
			if a + b + c <= n:
				count += 1

	return count

for i in [10,20,30,40,50,100,200,300,500,1000, 10000,20000]: print(i,generator251v5(i))

#for i in [10,20,30,40,50,100,1000,2000,10000]: print(i,generator251v5(i))

#print(generator251v5(10**7))
