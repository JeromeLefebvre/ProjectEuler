#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=36
Double-base palindromes
Problem 36
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''



def isBinaryPalindrome(n):
	'''Returns True if a number is a palindrome in base 2'''
	return bin(n)[2:][::-1] == bin(n)[2:]

def numberFromlist(c):
	total = 0
	n = 0
	for a in c:
		total += a*10**(len(c) - n - 1)
		n += 1
	return total

def problem36():
	from itertools import combinations_with_replacement, permutations
	# we have some duplicates 
	seen = set()
	for n in range(1,4):
		for c in combinations_with_replacement(range(0,10),n):
			for d in permutations(c,n):
				m = numberFromlist(d + d[::-1])
				if isBinaryPalindrome(m):
					seen.add(m)
				m = numberFromlist(d[:-1] + d[::-1])
				if isBinaryPalindrome(m):
					seen.add(m)
	return sum(seen)

def problem36a():
	from projectEuler import isPalindrome, isBinaryPalindrome
	# need to only check odd numbers as even numbers can never be bianry palidromes
	return sum([i for i in range(1,10**6,2) if isPalindrome(i) and isBinaryPalindrome(i)])


from cProfile import run
if __name__ == "__main__":
	print(problem36() == 872187)
	run("problem36()")
	print(problem36a()) 
	print(problem36a() == 872187)
	run("problem36a()")	
 
