#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=173
Using up to one million tiles how many different "hollow" square laminae can be formed?
Problem 173
Published on Saturday, 22nd December 2007, 05:00 am; Solved by 5124

'''

'''
Notes on problem 17():
'''

def problem173():
	GOAL = 10**6
	count = 0
	for t in range(1,10**3):
		for l in range(1,GOAL//(4*t)):
			if t**2 + t*l <= GOAL//4:
				count += 1
	return count


from cProfile import run
if __name__ == "__main__":
	#run("problem173()")
	print(problem173()) 