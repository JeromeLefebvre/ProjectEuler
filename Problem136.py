
#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=136
Singleton difference
Problem 136
'''

'''
Notes on problem 136():
'''

from collections import defaultdict

def problem136():
	found = defaultdict(int)
	goal = 5*10**7
	for u in range(1,goal+1):
		for v in range(u//3+1, goal // u + 1):
			if (u + v) % 4 == 0 and (3*v - u) % 4 == 0:
				found[u*v] += 1

	return sum( 1 for key in found if found[key] == 1)


from cProfile import run
if __name__ == "__main__":
	#run("problem136()")
	print(problem136()) 


