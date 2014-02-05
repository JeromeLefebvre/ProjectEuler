

from operator import mul
from functools import reduce
from copy import copy

def multiply(list):
	return reduce(mul, list, 1)


def cube(l):
	prod = multiply([a + 1 for a in l])
	print(prod)
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

