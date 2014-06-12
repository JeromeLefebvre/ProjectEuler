#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=230
Fibonacci Words
Problem 230
'''

'''
Notes on problem 230():
'''

def D(A,B):
	yield A
	while True:
		A, B = B, A+B
		yield A

def problem230():
	n = 0
	total = 0
	for a in D(list(str(1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679)), list(str(8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196))):
		if len(a) > (127+19*n)*7**n:
	 		total += 10**n*int(a[(127+19*n)*7**n])
	 		print(n)
	 		n += 1
	 		if n>17:
	 			return total


from cProfile import run
if __name__ == "__main__":
	#run("problem230()")
	print(problem230()) 