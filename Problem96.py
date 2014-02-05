#!/usr/local/bin/python3.3

'''
Problem 96
Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called Latin Squares. The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical starting puzzle grid and its solution grid.


A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary to employ "guess and test" methods in order to eliminate options (there is much contested opinion over this). The complexity of the search determines the difficulty of the puzzle; the example above is considered easy because it can be solved by straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid; for example, 483 is the 3-digit number found in the top left corner of the solution grid above.
'''

'''
Notes on problem 96():
	data = "0 0 3 0 2 0 6 0 0
9 0 0 3 0 5 0 0 1
0 0 1 8 0 6 4 0 0
0 0 8 1 0 2 9 0 0
7 0 0 0 0 0 0 0 8
0 0 6 7 0 8 2 0 0
0 0 2 6 0 9 5 0 0
8 0 0 2 0 3 0 0 9
0 0 5 0 1 0 3 0 0"
'''

def solveSudoku(sudoku,x=0,y=0):
	#printPuzzle(sudoku)
	#print()
	if not valid(sudoku):
		return False
	# Find the next available position
	#printPuzzle(sudoku)
	while sudoku[x][y] != 0:
		x += 1
		if x == 9:
			x = 0
			y += 1
			if y == 9:
				return True

	#for i in possibilities(sudoku, x,y):
	for i in range(1,10):
		sudoku[x][y] = i
		solved = solveSudoku(sudoku,x,y)
		if solved:
			return True
	sudoku[x][y] = 0
	return False

def row(sudoku,i):
	return [ sudoku[i][l] for l in range(0,9) ]

def col(sudoku,j):
	return [ sudoku[l][j] for l in range(0,9) ]

def square(sudoku, x, y):
	x, y = whichSquare(x,y)
	return [sudoku[x][y + j] for j in range(0,3)] + [sudoku[x+1][y + j] for j in range(0,3)] + [sudoku[x+2][y + j] for j in range(0,3)]

def whichSquare(x,y):
	if 0 <= x < 3:
		if 0 <= y < 3:
			return (0,0)
		if 3 <= y < 6:
			return (3,0)
		if 6 <= y < 9:
			return (6,0)
	if 3 <= x < 6:
		if 0 <= y < 3:
			return (0,3)
		if 3 <= y < 6:
			return (3,3)
		if 6 <= y < 9:
			return (6,3)
	if 6 <= x < 9:
		if 0 <= y < 3:
			return (0,6)
		if 3 <= y < 6:
			return (3,6)
		if 6 <= y < 9:
			return (6,6)

def possibilities(sudoku,x,y):
	l = {1,2,3,4,5,6,7,8,9}
	l = l.difference( set(row(sudoku, x)))
	l = l.difference( set(col(sudoku, y)))
	l = l.difference( set(square(sudoku,x,y)))
	return l

def printPuzzle(sudoku):
	for j in range(0,9):
		print([sudoku[j][i] for i in range(0,9)])
def valid(sudoku):
	# checking each line
	for i in range(0,9):
		if any( row(sudoku,i).count(a) > 1 for a in range(1,10)): return False

	# Checking each row
	for j in range(0,9):
		if any( col(sudoku,j).count(a) > 1 for a in range(1,10)): return False
	# checking each square
	for square in [(0,0), (3,0), (6,0), (0,3),(3,3), (6,3), (0,6),(3,6),(6,6)]:
		x, y = square
		l = [sudoku[x][y + j] for j in range(0,3)] + [sudoku[x+1][y + j] for j in range(0,3)] + [sudoku[x+2][y + j] for j in range(0,3)]
		if any(l.count(i) > 1 for i in range(1,9)): return False
	return True


def problem96():
	total = 0
	with open("Problem96.txt",'r') as sudokuData:
		for puzzle in range(0,50):
			sudoku = []
			for i in range(0,10):
				r = sudokuData.readline()
				if i == 0:
					pass
				if i > 0:
					sudoku.append( [int(r[i]) for i in range(0,9)] )
			#sudoku = [ [int(r) for r in row.split(' ')] for row in data.split('\n')]
			solveSudoku(sudoku)
			print(puzzle)
			printPuzzle(sudoku)
			total += int(str(sudoku[0][0]) + str(sudoku[0][1]) + str(sudoku[0][2]))

	return total



if __name__ == "__main__":
	print(problem96())
 