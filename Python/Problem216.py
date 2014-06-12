#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=216
Investigating the primality of numbers of the form 2n2-1
Problem 216
'''

'''
Notes on problem 216():
'''

from itertools import count

def t(goal):
	for n in count(2):
		yield 2*n**2 - 1
		if n >= goal:
			break

from PE_primes import isPrime, iPrime, factorize

def problem216():
	count = 0
	for p in iPrime():
		print(jacobi(( p + 1)//2, p))
		if p > 100: break
	return
	for index, n in enumerate(t(100)):
		index += 2
		#print( 2*(index)**2 -1 , n, isPrime(n), jacobi(( index + 1)//2, index))
		if isPrime(n):
			count += 1
			print("gave a prime ", jacobi(( n + 1)//2, n))
		else:
			for p in factorize(n):
				print("Didn't give a prime", p,jacobi(( p + 1)//2, p))
	return count

def jacobi(n, m):
    j = 1
    # rule 5
    n %= m
    while n:
        # rules 3 and 4
        t = 0
        while not n & 1:
            n //= 2
            t += 1
        if t&1 and m%8 in (3, 5):
            j = -j
        # rule 6
        if (n % 4 == m % 4 == 3):
            j = -j
        # rules 5 and 6
        n, m = m % n, n 
    return j if m == 1 else 0

from cProfile import run
if __name__ == "__main__":
	#run("problem216()")
	print(problem216()) 