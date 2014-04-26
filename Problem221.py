
'''
http://projecteuler.net/problem=221
Alexandrian Integers
Problem 221
'''

'''
Notes on problem 221():
'''

from itertools import count

def integers():
	for n in count(1):
		yield n
		yield -n

def problem221():
	found = []
	for p in integers():
		for q in range(-abs(p),abs(p)):
			if p == -q or q == 0: continue
			if (1-p*q) % (p + q) == 0:
				r = (1 - p*q) // (p + q)
				A = p*q*r
				if A not in found and A>0:
					found.append(A)
				if len(found) >= 15*10**4:
					found.sort()
					print(found[15*10**4-1])


from cProfile import run
if __name__ == "__main__":
	#run("problem221()")
	print(problem221()) 