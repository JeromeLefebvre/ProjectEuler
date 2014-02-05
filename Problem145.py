#!/usr/local/bin/python3.3

'''
Problem 145
Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (109)?
'''

'''
Notes on problem 145():
'''
def isReversible(n):
	s = n + int(str(n)[::-1])
	return set(str(s)) <= {'1','3','5','7','9'}

def problem145a():
	GOAL = 10**6
	l = []
	count = 0
	for n in range(1,GOAL):
		if n % 10 != 0 and isReversible(n):
			#print(n,int(str(n)[::-1]),n + int(str(n)[::-1]))
			#l.append(n)
			count += 1
	return count

def problem145():
	count = 0
	# 1 digits There are no solutions as a + a = 2a is even
	# 2 digits
	for start in [2*l + 1 for l in range(0,5)]:
		for end in [2*l for l in range(1,5)]:
			s = start*10 + end
			if isReversible(s):
				count += 1
	# 3 digits if we let E to be even, O for odd then
	# EaO + OaE = (E+O) + (2a) + (E + O), so we need E+O to have a carry
	# 
	for start in range(1,10,2):
		for end in range(0,10,2):
			for i in range(0,10**1):
				s = start*10**(len(str(i))+1) + i*10 + end
				if isReversible(s):				
					count += 1
	#print([i for i in range(1,10**3) if isReversible(i) and (i)% 10 != 0])
	#count2 = sum([1 for i in range(1,10**6) if isReversible(i) and (i)% 10 != 0])
	return count*2

if __name__ == "__main__":
	print(problem145())
 