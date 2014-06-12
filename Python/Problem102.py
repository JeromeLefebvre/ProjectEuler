#!/usr/local/bin/python3.3

'''
Problem 102
Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of one thousand "random" triangles, find the number of triangles for which the interior contains the origin.

NOTE: The first two examples in the file represent the triangles in the example given above.
'''

'''
Notes on problem 102():
'''
from projectEuler import primes
from vector import vector, perp,projectOnto,distanceSqrd, lengthSqrd
from itertools import combinations
def intersectionOfTwoLines(p1,p2,p3,p4):
	''' The intersetion of the two lines spanned by p1,p2 and by p3,p4'''
	x1,y1,x2,y2,x3,y3,x4,y4 = p1.x,p1.y,p2.x,p2.y,p3.x,p3.y,p4.x,p4.y
	denominator = (x1 - x2)*(y3-y4) - (y1-y2)*(x3-x4)
	numeratorx = (x1*y2 - y1*x2)*(x3-x4) - (x1 - x2)*(x3*y4 - y3*x4)
	numeratory = (x1*y2 - y1*x2)*(y3-y4) - (y1 - y2)*(x3*y4 - y3*x4)
	return vector(numeratorx,numeratory)/denominator

def area(a,b,c):
	# (a[0] - c[0])*(b[1] -a[1]) - (a[0]-b[0])*(c[1]-a[1]));
	return abs((a.x - c.x)*(b.y - a.y) - (c.y - a.y)*(a.x - b.x))

def orthogonalIntersection(v,w,p):
	'''Does the line orthogonal to the one going from v to w intersects the line segment between v and w'''
	m = vector(v.x - w.x, v.y - w.y)
	r = intersectionOfTwoLines(v,w,p,perp(m))

	return 0 <= distanceSqrd(v,r) <= distanceSqrd(v,w)

def problem102():
	count = 0
	zero = vector(0,0)
	with open('Problem102.txt','r') as data:
		for l in data.readlines():
			x0,x1,y0,y1,z0,z1 = l.split(',')
			X, Y, Z = vector(x0,x1),vector(y0,y1),vector(z0,z1)
			# Computes the area of each of the possible inner trianle and compares it to the area of the centre
			if area(X,Y,Z) == area(X,Y,zero) + area(X,zero,Z) + area(zero,Y,Z):
				count += 1
	#return all(orthogonalIntersection(v,w, vector(0,0)) for v,w in combinations([X,Y,Z],2))
	return count


if __name__ == "__main__":
	print(problem102())
 