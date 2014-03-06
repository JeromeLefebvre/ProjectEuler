

from itertools import chain, combinations
def powerset(A):
  return chain.from_iterable( combinations(A,n) for n in range(len(A)+1) )

def isSpecialSum(A):
	for B,C in combinations(powerset(A),2):
		if sum(B) == sum(C):
			return False
		if len(B) < len(C) and sum(B) > sum(C):
			return False
	return True

from random import randint
def newSet(A):
	index = randint(0,len(A)-1)
	offset = randint(-2, 1)
	if A[index] + offset not in A:
		A[index] += offset
'''
If things work out we should see this...
[22, 33, 40, 41, 42, 44, 47]
[21, 33, 40, 41, 42, 44, 47]
[20, 33, 40, 41, 42, 44, 47]
[20, 32, 39, 40, 41, 43, 46]
[20, 31, 38, 39, 40, 42, 45]
'''
import copy
def problem103():
	#A = {21,11+21, 18+21, 19+21, 20+21, 22+21, 25+21}
	A = [22,11+22, 18+22, 19+22, 20+22, 22+22, 25+22]
	record = A
	A.sort()
	print(A)
	for i in range(1,1000):
		B = copy.copy(record)
		for j in range(1,50):
			newSet(B)				
			if sum(B) < sum(record) and isSpecialSum(B):
				record = B
				record.sort()
				print(record)
				break
	return int(''.join([str(a) for a in record]))


if __name__ == "__main__":
	print(problem103() == 20313839404245)
 