'''
http://projecteuler.net/problem=139
Pythagorean tiles
Problem 139
'''

'''
Notes on problem 139():
'''

def problem139():
	result = 0
	limit = 100000000
	x = 1
	y = 1
	 
	while(x+y < limit):
	    xnew = 3 * x + 4 * y
	    ynew = 2 * x + 3 * y
	    x = xnew
	    y = ynew
	    result += limit // (x + y)
	return result


from cProfile import run
if __name__ == "__main__":
	#run("problem139()")
	print(problem139()) 

