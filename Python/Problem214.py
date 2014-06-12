#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=214
Totient Chains
Problem 214
'''

'''
Notes on problem 214():
'''

def computeAllPhi():
    goal = 40000000
    phi = list(range(0,goal+1))
    for n in range(2,goal+1):
        if n == phi[n]: # n is prime
            for i in range(n,goal+1,n):
                phi[i] *= (n - 1)/n
        phi[n-1] = int(phi[n-1])
    return phi

from PE_primes import primesUpTo
def problem214():
	total = 0
	phi = computeAllPhi()
	def lengthOfChain(n,_d={1:1}):
		if n not in _d:
			_d[n] = lengthOfChain(phi[n]) + 1
		return _d[n]
	for p in primesUpTo(40000000):
		if lengthOfChain(p) == 25:
			total += p
	return total


from cProfile import run
if __name__ == "__main__":
	#run("problem214()")
	print(problem214()) 


