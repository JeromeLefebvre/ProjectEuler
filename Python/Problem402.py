
# Problem 402

from fractions import gcd
from functools import reduce
from operator import mul
from copy import copy
from itertools import product

def gcdd(*args):
	return reduce(gcd,args)

def M(a,b,c):
	return gcdd(*[n**4 + a*n**3 + b*n**2 + c*n for n in range(1,5)])

def S(N):
	return sum([M(a,b,c) for a,b,c in product(range(1,N+1),repeat=3)])

def M2(a,b,c):
	return gcdd(24,6*(a+6),2*(b-11),a+b+c+1)

def M3(a,b,c):
	return gcdd(24, 6*(a+2),2*(b+1), a+b+c+1)

def M4(a,b,c):
	return gcdd(24, a+b+c+1, 2*gcd(3*(a+2),(b+1)))


# 16.757 seconds
def M5(a,b,c):
	if (a + 2) % 4 == 1 or (a + 2) % 4 == 3:
		return gcd(2*gcd(3,b+1), a+b+c+1)
	if (a + 2) % 4 == 0:
		return gcd(2*gcd(b+1,12),a+b+c+1)
	if (a + 2) % 4 == 2:
		return gcd(2*gcd(b+1,6),a+b+c+1)

#N = 200   11.947
def M6(a,b,c):
	if (a + 2) % 4 == 1 or (a + 2) % 4 == 3:
		if (b + 1) % 3 == 0:
			# gcd(6, a+b+c+1)
			if (a + b + c + 1) % 2 == 0:
				if (a + c) % 3 == 0:
					return 6
				return 2
			if (a + c)% 3 == 0:
				return 3
			return 1

		if (a+b+c+1) % 2 == 0:
			return 2
		return 1
	if (a + 2) % 4 == 0:
		return gcd(2*gcd(b+1,12),a+b+c+1)
	if (a + 2) % 4 == 2:
		return gcd(2*gcd(b+1,6),a+b+c+1)



for a,b,c in product(range(1000,1010),repeat=3):
	#if M4(a,b,c) != M6(c,b,a): print(a,b,c,M(a,b,c),M5(a,b,c))
	M(a,b,c)
