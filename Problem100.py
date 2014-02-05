#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=100
Arranged probability
Problem 100
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 1012 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.
'''

'''
Notes on problem 100():
'''
from projectEuler import solveIntegerQuadratic

def problem100():
	for b in range(1,100):
		if isSquare(  (-1 - 2*b)**2 - 4*(b - b**2)  ):
			d = (int)((-1 - 2*b)**2 - 4*(b - b**2))
			As = []
			if (1 + 2*b - d) % 2 == 0 and (1 + 2*b - d) > 0:
				As.append((1 + 2*b - d)//2)
			if (1 + 2*b + d) % 2 == 0 and (1 + 2*b + d) > 0:
				As.append((1 + 2*b + d)//2)
			for a in As:
				print(a,b, a/(a+b)*(a-1)/(a+b-1))

def problem100():
	# By expanding a/(a+b) * (a-1)/(a+b - 1) = 1/2
	# we get the 2 variable polynomials: a**2 - 2*a*b - b**2 - a + b = 0
	# We then get generators from : http://www.alpertron.com.ar/QUAD.HTM
	# x_{n+1} = 5 x_n + 2 y_n - 2
	# y_{n+1} = 2 x_n + y_n -1
	'''
	for b in range(1,10**12):
		for a in [a for a in solveIntegerQuadratic(1,-1-2*b, b -b**2) if a > 0]:
			print(a,b)
	'''

	x = 3
	y = 1
	while x + y < 10**12:
		x,y  = 5*x + 2*y - 2, 2*x + y - 1
	return x
if __name__ == "__main__":
	print(problem100() == 756872327473)
 