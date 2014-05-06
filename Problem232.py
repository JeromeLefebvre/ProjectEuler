'''
http://projecteuler.net/problem=232
The Race
Problem 232
'''

'''
Notes on problem 232():
'''

from itertools import count, combinations
import random
import math

def problem232():
	games = 0
	while True:
		A_score = 0
		B_score = 0
		for r in count():
			if A_score >= 100 or B_score >= 100:
				print(A_score, B_score)
				if B_score > A_score:
					return
				break
			# A's turn
			if random.choice(['H','T']) == 'H':
				A_score += 1
			T = random.randint(1, int(math.log(100-B_score,2)))
			if random.choice([c for c in combinations(['H','T']*T, T)]) == ('T',)*T:
				B_score += 2**(T-1)

from cProfile import run
if __name__ == "__main__":
	#run("problem232()")
	print(problem232()) 