#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=142()
Perfect Square Collection
Problem 142
Find the smallest x + y + z with integers x > y > z > 0 such that x + y, x − y, x + z, x − z, y + z, y − z are all perfect squares.
'''

'''
Notes on problem 142():
'''
from projectEuler import isSquare

'''
The various equations:
x + y = a1
x - y = a2
x + z = a3
x - z = a4
y + z = a5
y - z = a6

then
a1 - a3 = (x + y) - (x + z) = y - z = a6
a3 + a4 = (x + z) + (x - z) = 2x 
a5 = y + z = (x+y) - (x - z) = a1 - a4
a2 = x - y = (x + z) - (y + z) = a3 - a5
a3 - a4 = (x+z) - (x - z) = 2z > 0
'''
def problem142():
	i = 1
	record = 7691793
	while True:
		a1 = i**2
		# we need a1 - a3 = a6 > 0
		for j in range(2,i):
			a3 = j**2
			if isSquare(a1 - a3):
				# a6 is positive
				a6 = a1 - a3
				# need now that a3 and a4 have the same parity as a4 + a3 = 2x
				for k in range(j%2,j,2):
					a4 = k**2
					a5 = a1 - a4
					a2 = a3 - a5
					if a2 > 0 and a5> 0 and isSquare(a5) and isSquare(a2):
						if (a1 + a2) % 2 == 0 and (a5 + a6) % 2 == 0 and (a3 - a4) % 2 == 0:
							x = (a1 + a2)//2
							y = (a5 + a6)//2
							z = (a3 - a4)//2
							if x + y + z < record and x > y and y > z and z>0 and all([isSquare(x-y), isSquare(x+y), isSquare(x+z), isSquare(x-z), isSquare(y+z), isSquare(y-z)]):
								return x + y + z

		i += 1
		print(i)


if __name__ == "__main__":
	print(problem142())
 