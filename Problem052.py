
'''
Problem52
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''

def sameDigits(a,b):
	return set(str(a)) == set(str(b)) and len(str(a)) == len(str(b))

def problem52():
	for n in range(2,10):
		for i in range(10**(n-1), 10**n//6 + 1):
			cyclic = True
			for l in range(2,7):
				if not sameDigits(i,l*i):
					cyclic = False
					break
			if cyclic:
				return i

def problem52a():
	for n in range(2,10):
		for i in range(10**(n-1), 10**n//6 + 1):
			if all(sameDigits(i,l*i) for l in range(2,7)):
				return i

from cProfile import run
if __name__ == "__main__":
	print(problem52() == 142857)
	run("problem52()")
	print(problem52a() == 142857)
	run("problem52a()")


