

'''
Problem 117
Using a combination of black square tiles and oblong tiles chosen from: red tiles measuring two units, green tiles measuring three units, and blue tiles measuring four units, it is possible to tile a row measuring five units in length in exactly fifteen different ways.

How many ways can a row measuring fifty units in length be tiled?

NOTE: This is related to problem 116.
'''

from math import factorial

n = 50

total = 0
for d in range(0,n//4+1):
	for c in range(0,(n-4*d)//3+1):
		for b in range(0,(n-4*d-3*c)//2+1):
			a = n - 4*d - 3*c - 2*b
			f = factorial(a+b+c+d)//( factorial(a)*factorial(b)*factorial(c)*factorial(d))
			total += f

print(total)
