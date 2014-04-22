'''
http://projecteuler.net/problem=138
Special isosceles triangles
Problem 138
'''

'''
Notes on problem 138():
Since I always forget how to deal with Pell equations, I went to get some help:
http://www.mathblog.dk/project-euler-138-special-isosceles-triangles/
'''

def problem138():
	total = 0
	x = 0
	y = -1
	for i in range(0,12):
	    x, y = -9 * x + -4 * y + 4, -20 * x + -9 * y + 8
	    total += abs(y)
	return total

from cProfile import run
if __name__ == "__main__":
	run("problem138()")
	print(problem138() == 1118049290473932) 