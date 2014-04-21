'''
http://projecteuler.net/problem=191
Prize Strings
Problem 191
'''

'''
Notes on problem 191():
'''

def problem191():
	def count(sofar=(,)):
		if sofar.count('L') == 2:
			return 0
		if len(sofar) > 2 and sofar[-3:] == ('A','A','A'):
			return 0
		if len(sofar) == 4:
			return 1
		total = 0
		for day in ['0','A','L']:
			total += count(sofar + (day,))
		return total
	return count()

def problem191():
	def count(sofar=()):
		if len(sofar) > 2 and sofar[-3:] == ('A','A','A'):
			return 0
		if len(sofar) == 30:
			return 1
		total = 0
		if not any(a == 'L' for a in sofar):
			total += count(sofar + ('L',))
		for day in ('0','A'):
			total += count(sofar + (day,))
		return total
	return count()


from cProfile import run
if __name__ == "__main__":
	#run("problem191()")
	# Currently takes a few hours
	print(problem191() == 1918080160) 