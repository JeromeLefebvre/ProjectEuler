

from projectEuler import factorize

for n in range(1,10**5):
	factorize(n)

def integerSquare(d):
	''' Expects a square integer '''
	s = int(sqrt(d))
	if d == s**2:
		return s
	return s+1