#!/usr/local/bin/python3.3

'''
Problem 62
The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''

'''
Notes on problem 62():
'''
from PE_sequences import iCube
from itertools import permutations

def numberOfContainedPermutations(n,L):
	seen = []
	for c in permutations([a for a in str(n)]):
		c = int(''.join(c))
		if len(str(c)) == len(str(n)) and c in L:
			seen.append(c)
	return set(seen)

def integerCube(n):
	'''Returns the cube root of an cubed interger'''
	d = int(n**(1/3))
	if d**3 == n:
		return d
	return d+1

def isCube(n):
	pass

def problem62():
	cubes = []
	length = 0
	for cube in iCube(10**13):
		if len(str(cube)) > length:
			for a in cubes:
				for b in cubes:
					if a != b and all([ str(a).count(p) == str(b).count(p) for p in set(str(a))]):
						for c in cubes:
							if a != c and b != c and c != a and all([ str(b).count(p) == str(c).count(p) for p in set(str(a))]):
								for d in cubes:
									if a != d and b != d and c != d and all([ str(c).count(p) == str(d).count(p) for p in set(str(a))]):
										for e in cubes:
											if a != e and b != e and c != e and d != e and all([ str(d).count(p) == str(e).count(p) for p in set(str(a))]):
												return min(a,b,c,d,e)

			cubes = []
			length = len(str(cube))
		cubes.append(cube)

def sameDigits(a,b):
	# Check if there is hope that they have the same digits, if not throw it away
	return set(str(a)) == set(str(b)) and all([ str(a).count(p) == str(b).count(p) for p in set(str(a))])

from PE_digits import numberOfDigits
from itertools import combinations
def problem62a():
	length = 0
	cubesOfInterest = []
	for cube in iCube(10**9):
		# The idea is we add all cubes in cubesOfInterest
		# Once we hit a new length for cube we check all possible 5 permutations of possible cubes
		# and check if they are all permutations of each other
		if numberOfDigits(cube) > length:
			print(len(cubesOfInterest))
			for d in cubesOfInterest:
				
				if all( sameDigits(d[0],d[i]) for i in range(1,3)):
					return min(d)
			length = numberOfDigits(cube)
			cubesOfInterest = []
		cubesOfInterest.append(cube)

def root3rd(x):
    y, y1 = None, 2
    while y!=y1:
        y = y1
        y3 = y**3
        d = (2*y3+x)
        y1 = (y*(y3+2*x)+d//2)//d
    return y

def isCube(n):
	return root3rd(n)**3 == n

def numberFromList(c):
	total = 0
	for n, a in enumerate(c):
		total += a*10**(len(c) - n - 1)
	return total

def problem62():
	from itertools import count
	length = 0
	cubesOfInterest = {}
	for cube in count(1):
		cube = cube**3
		digits = tuple(sorted([ a for a in str(cube)]))
		# The idea is we add all cubes in cubesOfInterest
		# Once we hit a new length for cube we check all possible 5 permutations of possible cubes
		# and check if they are all permutations of each other
		if len(digits) > length:
			# Since dictionaries entry aren't sorted, we could hit multiple pairs
			candidates = []
			for c in cubesOfInterest:
				if len(cubesOfInterest[c]) == 5:
					candidates.append(min(cubesOfInterest[c]))
			if candidates != []:
				return min(candidates)
			length += 1
			cubesOfInterest = {}
		if digits in cubesOfInterest:
			cubesOfInterest[digits].append(cube)
		else:
			cubesOfInterest[digits] = [cube]


from cProfile import run
if __name__ == "__main__":
	print(problem62() == 127035954683)
	run("problem62()")