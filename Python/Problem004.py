#!/usr/local/bin/python3.3

'''
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

from pe.digits import isPalindrome

# A palidrome made of 6 digits is an divisible by 11
# As abccba = a*10**5 + b*10**4 + c*10**3 + c*10**2 + b*10 + a = -a + b - c + c - b + a = 0 mod 11
# So, 11 divides either i or j.
# 6
'''Built-in functions such as max() and min() can take a single iterator argument and will return the largest or smallest element. 
The "in" and "not in" operators also support iterators: X in iterator is true if X is found in the stream returned by the iterator. 
You’ll run into obvious problems if the iterator is infinite; max(), min() will never return, and if the element X never appears in the stream, the "in" and "not in" operators won’t return either.

http://docs.python.org/3.3/howto/functional.html
'''

def problem4e():
	return max([max([i*j for j in range(100,1000) if isPalindrome(i*j)]+[0]) for i in range(990,100,-11)])

def problem4d():
	return max([max([prod for prod in range(0,999*i,i) if isPalindrome(prod)]) for i in range(121,1000,11)])

def problem4():
	return max([max([i*j for j in range(100,1000) if isPalindrome(i*j)]+[0]) for i in range(990,100,-11)])

def problem4a():
	#return max([max([i*j for j in range(100,1000) if isPalindrome(i*j)]+[0]) for i in range(110,1000,11)])
	return max(max( i*j for j in range(0,1000) if isPalindrome(i*j) ) for i in range(110,1000,11))

def problem4b():
	return max(prod for j in range(990,121,-11) for prod in range(3*j,999*j,j) if isPalindrome(prod))

def problem4b():
	return max([prod for j in range(40*11,990,11) for prod in range(600*j,999*j,j) if isPalindrome(prod)])

def problem4c():
	maximum = 0
	for i in range(110,1000,11):
		for j in range(0,999*i,i):
			if isPalindrome(j):
				maximum = max(maximum,j)
				if j == 995599:
					print(i)
	return maximum

from cProfile import run
if __name__ == "__main__":
	#print(problem4())
	#print(problem4() == 906609)
	#print(problem4a() == 906609)
	print(problem4b() == 906609)
	#print(problem4c() == 906609)
	#print(problem4d() == 906609)
	#print(problem4e() == 906609)
	#run("problem4()")
	#run("problem4a()")
	run("problem4b()")
	#run("problem4c()")
	#run("problem4d()")
	#run("problem4e()")