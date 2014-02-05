

from random import choice
def randomSort(L):
	if L == []: return L
	y = choice(L)
	return randomSort([x for x in L if x < y]) + [y] + randomSort([x for x in L if x > y])





from random import choice
def select(L,n):
	y = choice(L)
	print(y)
	less = [x for x in L if x < y]
	greater = [x for x in L if x > y]
	if len(less) == n - 1: return y
	if len(less) > n - 1: return select(less, n)
	return select(greater, n - len(less) - 1)





from random import randint
from fractions import gcd
def pollardRho(N):
	if N%2==0: return 2
	x,c,g = randint(1, N-1), randint(1, N-1), 1
	y = x
	def f(a): return (a**2 + c) %N
	while g==1:		
		x = f(x)
		y = f(f(y))
		g = gcd(x-y,N)
	return g