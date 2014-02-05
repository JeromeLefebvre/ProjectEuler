#!/usr/local/bin/python3.3

'''
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

from PE_digits import isPalindrome

# A palidrome made of 6 digits is an divisible by 11
# As abccba = a*10**5 + b*10**4 + c*10**3 + c*10**2 + b*10 + a = -a + b - c + c - b + a = 0 mod 11
# So, 11 divides either i or j.
# 6
def problem4():
	return max([max([i*j for j in range(100,1000) if isPalindrome(i*j)]+[0]) for i in range(110,1000,11)])

from cProfile import run
if __name__ == "__main__":
	print(problem4() == 906609)
	run("problem4()")