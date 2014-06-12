#!/usr/local/bin/python3.3

'''
Problem 87
The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28 = 2^2 + 2^3 + 2^4
33 = 3^2 + 2^3 + 2^4
49 = 5^2 + 2^3 + 2^4
47 = 2^2 + 3^3 + 2^4

n = a^2 + b^3 + c^4
How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
'''

'''
Notes on problem 87():
'''
from projectEuler import primes

def problem87():
	checker = primes(save=True,initial=False)
	seen = []
	GOAL  = 5*10**7
	for c in checker[1:(GOAL - 2**3 - 2**2)**(1/4)]:
		for b in checker[1:(GOAL - c**4 - 2)**(1/3)]:
			for a in checker[1:(GOAL - c**4 - b**3)**(1/2)]:
				seen.append(a**2 + b**3 + c**4)
					#print(a**2 + b**3 + c**4)
	return len(set(seen))





if __name__ == "__main__":
	print(problem87())
 