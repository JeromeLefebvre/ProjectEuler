#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=93
Arithmetic expressions
Problem 93
'''

'''
Notes on problem 93():
'''

from itertools import permutations, combinations_with_replacement

from operator import mul, truediv, add, sub
def possibilities():
	numbers = {}
	for d1,d2,d3,d4 in permutations([1,2,3,4],4):
		for oper1,oper2,oper3 in combinations_with_replacement([mul, truediv, add, sub],4):
			# There are now several ways of combining them ((1,2),3),4
			numbers.add(oper3(oper2(oper1(d1,d2),d3),d4))
			# There are now several ways of combining them (1,(2,3)),4
			numbers.add(oper3(oper1(oper2(d2,d3),d1),d4))
			# There are now several ways of combining them 1,((2,3),4)
			numbers.add(oper1(oper3(oper2(d2,d3),d4),d1))
			# There are now several ways of combining them 1,(2,(3,4))
			numbers.add(oper1(oper2(oper3(d3,d4),d2),d1))
			# There are now several ways of combining them (1,2),(3,4)
			numbers.add(oper2(oper1(d1,d2),oper3(d3,d4)))
	return numbers

def problem93():
	return possibilities()



if __name__ == "__main__":
	print(problem93())
 