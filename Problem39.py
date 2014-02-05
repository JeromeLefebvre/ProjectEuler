
'''
Problem39
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

''' I lost track of the algorithm and not sure why I need the *2 at the end'''

from projectEuler import isSquare, integerSquare

def problem39():
	GOAL = 1000
	values = {}
	for p in range(1,GOAL+1):
		values[p] = []
	# the bounds come from a + b > c, a < c, b < c and a + b + c <= 1000
	for a in range(1,GOAL//2):
		for b in range(1,(500-a)//2):
			if isSquare(a**2 + b**2):
				c = integerSquare(a**2 + b**2)
				values[a + b + c].append([a,b,c])
	record = 0
	recordp = 0
	for p in range(1,GOAL+1):
		if len(values[p])/2 > record:
			record = len(values[p])/2
			recordp = p
	return recordp*2

from cProfile import run
if __name__ == "__main__":
	print(problem39())
	run("problem39()")
