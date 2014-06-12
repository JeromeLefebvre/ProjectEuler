#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=220
Heighway Dragon
Problem 220
'''

'''
Notes on problem 220():
'''

def HeighwayDragon(string='Fa',n=0,maximum=10):
	if n == maximum+1:
		return
	for letter in string:
		if letter not in ['a','b']:
			yield letter
		elif letter == 'a':
			for r in HeighwayDragon(string='aRbFR',n=n+1,maximum=maximum): yield r
		elif letter == 'b':
			for r in HeighwayDragon(string='LFaLb',n=n+1,maximum=maximum): yield r

def add(position,direction):
	return position[0] + direction[0], position[1] + direction[1]

def problem220():
	position = (0,0)
	step = 0
	facing = 0
	directions = [(0,1),(1,0),(0,-1),(-1,0)]
	string = ''
	strings = {}
	for depth in range(0,10):
		for l in HeighwayDragon(maximum=depth):
			string += l
			if l == 'F':
				position = add(position,directions[facing])
				step += 1
				if step == 10**12: return string, position
			elif l == 'R':
				facing = (facing + 1) % 4
			elif l == 'L':
				facing = (facing - 1) % 4
		#print(string, string[::-1])
		strings[depth] = string
		string = ""
	for depth in range(1,9):
		#print(strings[depth])
		print(strings[depth] [len(strings[depth-1]):] )
	return string


from cProfile import run
if __name__ == "__main__":
	#run("problem220()")
	print(problem220()) 
