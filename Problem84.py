#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=84
Monopoly odds
Problem 84

'''

'''
Notes on problem 84():
'''
from projectEuler import *
from random import shuffle
from random import randint
class deck:
	def __init__(self,cards):
		self.cards = cards
		shuffle(self.cards)

	def draw(self):
		self.cards.insert(0,self.cards.pop())
		return self.cards[0]

class board:
	def __init__(self,communityChest,chance):
		self.position = 0
		self.spots = ['GO','A1','CC1','A2','T1','R1','B1','CH1','B2','B3','JAIL','C1','U1','C2','C3','R2','D1','CC2','D2','D3','FP','E1','CH2','E2','E3','R3','F1','F2','U2','F3','G2J','G1','G2','CC3','G3','R4','CH3','H1','T2','H2']
		self.history = {spot:0 for spot in self.spots}
		self.communityChest = communityChest
		self.chance = chance

	def move(self):
		roll = randint(1,4) + randint(1,4)
		self.position += roll
		if self.position > 39:
			self.position %= 40
		self.history[self.spots[self.position]] += 1
		if self.position in [self.spots.index('CC1'),self.spots.index('CC2'),self.spots.index('CC3')]:
			self.action(self.communityChest.draw())
		elif self.position == self.spots.index('G2J'):
			self.action('JAIL')
		elif self.position in [self.spots.index('CH1'),self.spots.index('CH2'),self.spots.index('CH3')]:
			self.action(self.chance.draw())

	def action(self, spot):
		if spot in ['JAIL','GO','C1','E3','H2','R1']:
			self.position = self.spots.index(spot)
			self.history[self.spots[self.position]] += 1
		elif spot == '-3':
			self.position -= 3
			if self.position < 0:
				self.position %= 40
			self.history[self.spots[self.position]] += 1
		elif spot == 'NR':
			if 5 < self.position <=15:
				self.position = 15
				self.history[self.spots[self.position]] += 1
			elif 15 < self.position <=25:
				self.position = 25
				self.history[self.spots[self.position]] += 1
			elif 25 < self.position <=35:
				self.position = 35
				self.history[self.spots[self.position]] += 1
			else:
				self.position = 5
				self.history[self.spots[self.position]] += 1
		elif spot == 'NU':
			if 13 < self.position <=29:
				self.position = 29
				self.history[self.spots[self.position]] += 1
			else:
				self.position = 13
				self.history[self.spots[self.position]] += 1
		elif spot == 'BLANK':
			pass
		else:
			print("missing action",spot)

	def statistic(self):
		history = [ (self.history[key],key) for key in self.history ]
		history.sort()
		history.reverse()
		history = [self.spots.index(history[i][1]) for i in range(0,3)]
		return history

def problem84():
	communityChest = deck(['GO','JAIL'] + ['BLANK']*14)
	chance = deck( ['GO','JAIL', 'C1','E3','H2','R1','NR','NR','NU','-3'])	
	b =  board(communityChest, chance)
	b.move()
	for i in range(1,10**7):
		b.move()
	a = b.statistic()
	return a[0]*10**4 + a[1]*10**2 + a[2]

from cProfile import run
if __name__ == "__main__":
	run("problem84()")
	# Not guaranteed to get the correct answer
	print(problem84() == 101524)
 