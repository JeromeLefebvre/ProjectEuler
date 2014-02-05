
import unittest 


def triangle(n):
	''' Returns the sum of the first n integers, expects the solution to be an integer'''
	# We expect a positive integers, anything else and the program calling this function made an error
	assert(n >= 0)
	return n*(n+1)//2

phi = (1 + 5**(1/2))/2

def fib(n,_fib={}):
	from math import sqrt
	''' This is the fibonacci squence starting from 1,1,2,3,5,...'''
	# There are even faster ways of computing this, see: http://en.literateprograms.org/Fibonacci_numbers_(Python)
	if n not in _fib:
		# pass n == 71, the accuracy drops enough that you start to generate errors.
		if n < 72:
			_fib[n] = int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))
		else:
			_fib[n] = fib(n-1) + fib(n-2)
	return _fib[n]


def sumOfSquares(n):
	'''Returns the sums of squares of the first n integers'''
	assert(n>= 0)
	return n*(n+1)*(2*n + 1)//6

############################################################################
########### Various iterator
############################################################################

def iFibonacci():
	''' An interator for the Fibonacci sequence 1,2,3,5'''
	a,b = 1,1
	while True:
		yield b
		a,b = b, a+b


from itertools import count

def iPentagonal(max=10**1000):
	n = 1
	while (n*(3*n - 1)/2) < max:
		yield n*(3*n - 1)//2
		n += 1

def iPentagonal(maxn=10**1000):
	for n in count():
		yield n*(3*n - 1)//2
		if n > maxn:
			return False

def iHexagonal(max=10**1000):
	n = 1
	while n*(2*n-1) < max:
		yield n*(2*n-1)
		n += 1

def iTriangle(max=10**1000):
	n = 1
	while (n*(n+1)//2) < max:
		yield n*(n+1)//2
		n += 1

def iSquare(max=10**1000):
	n = 1
	while n**2 < max:
		yield n**2
		n += 1

def iHeptagonal(max=10**1000):
	n = 1
	while n*(5*n - 3)//2 < max:
		yield n*(5*n -3)//2
		n += 1

def iOctagonal(max=10**1000):
	n = 1
	while n*(3*n - 2) < max:
		yield n*(3*n - 2)
		n += 1

def iCube(max=10**1000):
	n = 1
	while n**3 < max:
		yield n**3
		n += 1		


class TestSequenceFunctions(unittest.TestCase):
	def setUp(self):
		pass

	def test_triangle(self):
		self.assertEqual(triangle(0),0)
		self.assertEqual(triangle(10),sum(range(10+1)))
		self.assertRaises(AssertionError,triangle,-1)

	def test_fib(self):
		with open("Fib_data.txt","r") as FibonacciData:
			fib_test = {}
			for n in FibonacciData.readlines():
				key,value = n.split(':')
				fib_test[int(key)] = int(value)

		for i in range(1,200):
			self.assertEqual(fib(i),fib_test[i])

if __name__ == '__main__':
	unittest.main()

