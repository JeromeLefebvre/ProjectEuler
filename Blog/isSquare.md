A word on isSquare. It is tempting to use to simplify the code and pick only one version of isSquare, the floating point version or the pure integer version. But for this simplification, you are picking speed or correctness. But there is no reason to make that choice. Let's profile both versions 

	def isSquare(a):
		'''isSquare(int) -> int --  Returns the square root of a if a is a square in the positive integers, None otherwise'''
		if 0 <= a < 2**54:
			sr = int(a**(1/2))
			if sr**2 == a:
				return sr
		elif a < 2**54:
			x = a
			y = (x + a // x) // 2
			while y < x:
				x = y
				y = (x + a // x) // 2
			if x**2 == a:
				return x
		else:
			return False

	def isSquareFloat(a):
		'''isSquare(int) -> int --  Returns the square root of a if a is a square in the positive integers, None otherwise'''
		sr = int(a**(1/2))
		if sr**2 == a:
			return sr

	def isSquareInteger(a):
		x = a
		y = (x + a // x) // 2
		while y < x:
			x = y
			y = (x + a // x) // 2
		if x**2 == a:
			return x

	import cProfile
	cProfile.run("for n in range(1,10**7): isSquare(n)")
	cProfile.run("for n in range(1,10**7): isSquareFloat(n)")
	cProfile.run("for n in range(1,10**7): isSquareInteger(n)")