
'''
Problem 43
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
'''

'''
I am being stupid here, there restrictions on the number are huge
There should be a better way of generating them
For example:
d4d5d6=635 is divisible by 5
means the 6 digit is 0 or 5
d6d7d8=572 is divisible by 11
then d7d8 11,22,33,44,55,66,77,88,99, 507, 518, 529, 540, 551, 562, 573, 584, 595
>>> s = [removesLastnDigits(i,1) for i in range(1,1000,13) if i > 100]
>>> s
[10, 11, 13, 14, 15, 17, 18, 19, 20, 22, 23, 24, 26, 27, 28, 30, 31, 32, 33, 35, 36, 37, 39, 40, 41, 43, 44, 45, 46, 48, 49, 50, 52, 53, 54, 56, 57, 58, 59, 61, 62, 63, 65, 66, 67, 69, 70, 71, 72, 74, 75, 76, 78, 79, 80, 82, 83, 84, 85, 87, 88, 89, 91, 92, 93, 95, 96, 97, 98]

'''
from itertools import permutations
from projectEuler import numberFromList
from PE_digits import removesDigits

def SubStringDivisibility(number):
	for index,p in enumerate([2,3,5,7,11,13,17]):
		if not removesDigits(number,2+index,4+index) % p == 0:
			return False
	return True
 
def problem43():
	digits = {str(i) for i in range(0,10)}
	total = 0
	# a can't be zero
	for a in digits.difference('0'):
		# b can be any digit different than a
		for b in digits.difference(a):
			for c in digits.difference(a+b):
				# d is an even number
				for d in {'0','2','4','6','8'}.difference(a+b+c):
					for e in digits.difference(a+b+c+d):
						if int(c+d+e)%3 != 0: continue
						# f is divisible by 5
						for f in {'0','5'}.difference(a+b+c+d+e):
							for g in digits.difference(a+b+c+d+e+f):
								if int(e+f+g)%7 != 0: continue
								for h in digits.difference(a+b+c+d+e+f+g):
									if int(f+g+h)%11 != 0: continue								
									for i in digits.difference(a+b+c+d+e+f+g+h):
										if int(g+h+i)%13 != 0: continue	
										for j in digits.difference(a+b+c+d+e+f+g+h+i):
											if int(h+i+j)%17 != 0: continue
											total += int(a+b+c+d+e+f+g+h+i+j)
	return total

from cProfile import run
if __name__ == "__main__":
	print(problem43() == 16695334890)
	run("problem43()")

