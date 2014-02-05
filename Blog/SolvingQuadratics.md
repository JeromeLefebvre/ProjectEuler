
In project Euler it is common to find integer roots to quadratic equations with integer coefficients. For example, if we want to check if a is a triangle number number, that is, is does there exists a positive integer n such that a = n*(n+1)/2? We can rewrite the equation as n^2 + n - 2a = 0. So given a, we are looking for positive integer solutions to a quadratic polynomials. First, let's look at the isTriangle function:

	def isTriangle(a):
		'''isTriangle(int) -> bool -- True if there is a solution to a = n*(n+1)/2 in the positive integers'''
		return any(n >= 0 for n in solveIntegerQuadratic(1,1,-2*a))

Now we have the function that finds the possible solutions:

	def solveIntegerQuadratic(a,b,c):
		''' solveIntegerQuadratic(int,int,int) -> list -- Returns a list (sorted by size and possibly empty) of all possible integer roots (with multiplicity)  to the quadratic polynomial of the form ax^2 + bx + c'''
		# Note, this is now a pure integer solution
		# If a is zero, then we simply have a linear polynomial
		if a == 0:
			return solveIntegerLinear(b,c)
		disc = b**2 - 4*a*c # The usual discriminant
		soln = []
		# We take the integer square of the disc
		sd = isSquare(disc)
		# We need to worry about the zero solution as 0 == False in python
		if sd == 0 or sd:
			# The two possible solutions
			if (-b - sd) % (2*a) == 0:
				soln.append((-b - sd) // (2*a))
			if (-b + sd) % (2*a) == 0:
				soln.append((-b + sd) // (2*a))
		soln.sort()
		return soln

So, the idea is simple. To solve a quadratic we need to check if the discriminant is positive, if it is, then we need to make sure it is a square. So, let's look at how to do it:

	def isSquare(a):
		'''isSquare(int) -> int --  Returns the square root of a if a is a square in the positive integers, None otherwise'''
		# If a is a small number, then we can do this quick version
		if 0 <= a <= 10**30:
			sr = int(a**(1/2))
			if sr**2 == a:
				return sr
		# If a is large number, due to loss of precision, we use a purely integer solution, which is slower
		else:
			# Our first guess is that x is 'halfway' between 0 and n
			x = a
			y = (x + a // x) // 2
			while y < x:
				# Here we take the average between x and a//x and this becomes out new x
				# with this, at every step x and a//x both approach the square root of n
				# x from above, a//x from below
				# y stands for the previous step
				x = y
				y = (x + a // x) // 2
			if x**2 == a:
				return x

This is wordier then one would expect, this is a trade off of speed, if a is small then:

	>>> a = 94873917982173987129849872193791278**2
	>>> a
	9001060313288276633698630988495225633485673626914701323587891428873284
	>>> int(a**(1/2))**2 == a
	False
	>>> a**(1/2)**2
	3.080161001996064e+17	


We also had the special case in which we needed to find roots of linear polynomials:

	def solveIntegerLinear(a,b):
		''' solveIntegerLinear(int, int) -> list -- Returns the integer solution to ax + b = 0 or an empty list'''
		# all integers are solutions to 0x = 0
		# so there is no good outputs to this
		if a == 0 and b == 0:
			raise ValueError
		if -b % a == 0:
			return [-b//a]
		return []

In the code, I also include a battery of tests to make sure that everything behaves as is.