
'''
Problem 40
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''

def problem40():
	Champernowne = []
	for i in range(1,200000):
		Champernowne.append(str(i))
	digits = {}
	position = 1
	for word in Champernowne:
		for letter in word:
			digits[position] = letter
			position += 1
	return int(digits[1])*int(digits[10])*int(digits[100])*int(digits[1000])*int(digits[10000])*int(digits[100000])*int(digits[1000000])

def digits(m):
	M = []
	while m > 0:
		M.append(m%10)
		m //= 10
	M.reverse()
	return M

def problem40a():
	Champernowne = []
	for i in range(1,200000):
		Champernowne += digits(i)
	return Champernowne[1-1]*(Champernowne[10-1])*(Champernowne[100-1])*(Champernowne[1000-1])*(Champernowne[10000-1])*(Champernowne[100000-1])*(Champernowne[1000000-1])

from cProfile import run
if __name__ == "__main__":
	print(problem40() == 210)
	run("problem40()")
	print(problem40a())
	print(problem40a() == 210)
	run("problem40a()")	
