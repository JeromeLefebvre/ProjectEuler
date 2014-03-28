from fractions import gcd
from functools import reduce

def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b // gcd(a, b)

def lcmm(*args):
	return reduce(lcm, args)

def gcdd(*args):
	return reduce(gcd, args)

from operator import mul
def product(args):
	return reduce(mul, args, 1)

from fractions import Fraction
from functools import reduce

def nCk(n,k):
	return int( reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1) )

def powerset(A,nonTrivial=False):
	''' powerset(set) -> iterator -- returns a complete list of all subsets of A as tuple, if nonTrivial=True, returns all set expects the empty set and A'''
	from itertools import chain, combinations
	if nonTrivial:
		return chain.from_iterable( combinations(A,i) for i in range(1,len(A)) )
	else:	
		return chain.from_iterable( combinations(A,i) for i in range(0,len(A)+1) )

def order(a,n):
	'''Expects (a,n) = 1, returns min k such that a^k = 1 mod n'''
	k = 1
	while a**k % n != 1:
		k+= 1
	return k
	
import unittest
class TestBasicFunctions(unittest.TestCase):
	def setUp(self):
		pass

	def test_gcd(self):
		self.assertEqual(gcd(4,6),2)
		self.assertEqual(gcdd(4,6,8),2)
		self.assertEqual(gcdd(*[4,6,8]),2)

	def test_powerset(self):
		self.assertEqual(list(powerset((1,2,3))), [(),(1,),(2,),(3,),(1,2),(1,3),(2,3),(1,2,3)])
		self.assertEqual(list(powerset((1,2,3),True)), [(1,),(2,),(3,),(1,2),(1,3),(2,3)])

if __name__ == "__main__":
	unittest.main()