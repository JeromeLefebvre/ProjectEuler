
'''
Problem 41
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

def numberFromList(c):
	n = 0
	total = 0
	for a in c:
		total += a*10**(len(c) - n -1)
		n += 1
	return total

def problem41():
	from itertools import permutations
	from PE_primes import isPrime
	# Let's just go over all the 7 digits pandigital numbers in reverse and find the first one that is prime
	for c in permutations(range(7,0,-1),7):
		if isPrime(numberFromList(c)):
			return numberFromList(c)

def problem41a():
	from projectEuler import isPandigital
	from PE_primes import primesUpTo
	# can avoid 8 digits and 9 digits as sum(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8) is divisible by 3 and thus so is the numbers with 9 digits
	return max( p for p in primesUpTo(10**7) if isPandigital(p) )


from cProfile import run
if __name__ == "__main__":
	print(problem41() == 7652413)
	run("problem41()")
	print(problem41a() == 7652413 )
	run("problem41a()")	
