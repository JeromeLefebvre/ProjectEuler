#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=93
Arithmetic expressions
Problem 93
'''

'''
Notes on problem 93():
'''

from itertools import permutations, combinations_with_replacement, combinations

from operator import mul, truediv, add, sub

def lengthOfSequence(numbers):
	record = 0
	for a,b in combinations([i for i in range(1,len(numbers))],2):
		if b-a > record and b-a == numbers[b] - numbers[a]:
			record = b -a
	return record + 1


def possibilities(l):
	numbers = []
	for d1,d2,d3,d4 in permutations(l,4):
		for oper in combinations_with_replacement([mul, truediv, add, sub],3):
			for oper1,oper2,oper3 in permutations(oper,3):
				# There are now several ways of combining them ((1,2),3),4
				try:
					numbers.append(oper3(oper2(oper1(d1,d2),d3),d4))
				except:
					pass
				try:
					numbers.append(oper3(oper2(d3,oper1(d1,d2)),d4))
				except:
					pass
				try:
					numbers.append(oper3(d4,oper2(d3,oper1(d1,d2))))
				except:
					pass
				try:
					numbers.append(oper3(d4,oper2(oper1(d1,d2),d3)))
				except:
					pass
				try:
					numbers.append(oper3(oper1(oper2(d2,d3),d1),d4))
				except:
					pass
				# There are now several ways of combining them (1,(2,3)),4
				try:
					numbers.append(oper3(oper1(d1,oper2(d2,d3)),d4))
				except:
					pass
				try:
					numbers.append(oper3(d4,oper1(oper2(d2,d3),d1)))
				except:
					pass
				try:
					numbers.append(oper3(d4,oper1(d1,oper2(d2,d3))))			
				except:
					pass				
				# There are now several ways of combining them 1,((2,3),4)
				try:
					numbers.append(oper1(oper3(oper2(d2,d3),d4),d1))
				except:
					pass
				try:
					numbers.append(oper1(oper3(d4,oper2(d2,d3)),d1))
				except:
					pass
				try:
					numbers.append(oper1(d1,oper3(oper2(d2,d3),d4)))
				except:
					pass
				try:
					numbers.append(oper1(d1,oper3(d4,oper2(d2,d3))))
				except:
					pass															
				# There are now several ways of combining them 1,(2,(3,4))
				try:
					numbers.append(oper1(oper2(oper3(d3,d4),d2),d1))
				except:
					pass						
				try:
					numbers.append(oper1(d1,oper2(oper3(d3,d4),d2)))
				except:
					pass						
				try:
					numbers.append(oper1(oper2(d2,oper3(d3,d4)),d1))
				except:
					pass						
				try:
					numbers.append(oper1(d1,oper2(d2,oper3(d3,d4))))
				except:
					pass						
															
				# There are now several ways of combining them (1,2),(3,4)
				numbers.append(oper2(oper1(d1,d2),oper3(d3,d4)))
	numbers.sort()
	#print(numbers)
	numbers = list(set(int(n) for n in numbers if int(n) == n))
	numbers.sort()
	#print(numbers)
	return lengthOfSequence(numbers)

def problem93():
	record = 0
	for d in combinations([1,2,3,4,5,6,7,8,9],4):
		if possibilities(d) > record:
			record = possibilities(d) 
			print(d, record)
	


if __name__ == "__main__":
	print(problem93())
 