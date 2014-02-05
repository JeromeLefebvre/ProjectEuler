

'''
Problem 48
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.


Note: Python shines when dealing with integers
'''

def problem48():
	total = 0
	for n in range(1,1000+1):
		total += pow(n,n,10**10)
	return total% 10**10

from cProfile import run
if __name__ == "__main__":
	print(problem48() == 9110846700)
	run("problem48()")