#!/usr/local/bin/python3.3

'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
'''

# The solution is simply C(2n, n)
# You can see this by drawing a square of all the possible paths
# starting from the first row and then then couting what happens
# so in the box with coordinates x,y there is C(x+y,x) ways of getting there

from pe.basic import nCk
def problem15():
	return nCk(20+20,20)

from cProfile import run
if __name__ == "__main__":
	print(problem15() == 137846528820)
	run("problem15()")