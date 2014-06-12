
'''
Problem 32
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

def isPandigital(i,j):
	word = str(i) + str(j) + str(i*j)
	return set(word) == {str(i) for i in range(1,10)} and len(word) == 9

from math import log
def problem32():
	seen = set()
	# the bounds are base on need to have certain number of digits
	# and estimate (using log) how many digits the output would have
	for i in range(1,50):
		for j in range(i+50,2000):
			if isPandigital(i,j):
				seen.add(i*j)
	return sum(seen)


from cProfile import run
if __name__ == "__main__":
	print(problem32() == 45228)
	run("problem32()")
 

