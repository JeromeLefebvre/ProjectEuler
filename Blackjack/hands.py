
class Card:
	''' The card object is an object that holds a rank and a suite
	the suited is sorted as:
	clubs = 0, diamonds = 1, hearts = 2, spades = 3
	the ranks are:
	ace = 0, 1 = 1, 2 = 2, ... , 10 = 10, Jack = 11, Queen = 12, King = 13
	'''
	def __init__(self,rank=None,suite=None):
		self._ranks = {0: 'Ace', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10:'10', 11:'Jack', 12:'Queen', 13:'King'}
		# Ranks and suites are unique pairs so convinient to be able to look them up in the reverse direction
		self._ranks_reverse = {'Ace': 0, '10': 10, 'Jack': 11, 'King': 13, '6': 6, '7': 7, '4': 4, '5': 5, '2': 2, '3': 3, '1': 1, 'Queen': 12, '8': 8, '9': 9, 'A':0, 'Q':12, 'J': 11, 'K': 13}
		self._suites = {0:'Clubs', 1:'Diamonds', 2:'Hearts',3:'Spades'}
		self._suites_reverse = {'Spades': 3, 'Clubs': 0, 'Diamonds': 1, 'Hearts': 2, 'S':3, 'C': 0, 'D':1, 'H':2}
		# if you don't specify a rank, pick one at random
		if rank == None:
			from random import randint
			self._rank = randint(0,13)
		else:
			if type(rank) == type(0):
				# raises an AssertionError if not within the accepted range
				assert( 0 <= rank <= 13)
				self._rank = rank
			elif type(rank) == type(""):
				assert( rank in [ key for key in self._ranks_reverse ] )
				self._rank = self._ranks_reverse[rank]
			else:
				# Gave a weird input
				raise ValueError
		if suite == None:
			from random import randint
			self._suite = randint(0,3)
		else:
			if type(suite) == type(0):
				# raises an AssertionError if not within the accepted range
				assert( 0 <= suite <= 3)
				self._suite = suite
			elif type(suite) == type(""):
				assert( suite in [ key for key in self._suites_reverse ] )
				self._suite = self._suites_reverse[suite]
			else:
				# Gave a weird input
				raise ValueError
	def rank(self):
		'''A getter for the rank of the card '''
		return self._rank

	def suite(self):
		'''A getter for the suite of the card '''
		return self._suite

	def __eq__(self, other):
		# Must compare against a card
		if type(other) != type(self):
			return False
		return self.rank() == other.rank() # self.suite() == other.suite() ?

	def __ne__(self,other):
		assert(type(self) == type(other))
		return self.rank() == other.rank()

	def __gt__(self,other):
		if type(other) not in (type(self), type(0)):
			raise TypeError("unorderable types")
		if type(other) == type(self):
			return self.rank() > other.rank()
		elif type(ohter) == type(0):
			return self.rank() > other

	def __ge__(self,other):
		if type(other) not in (type(self), type(0)):
			raise TypeError("unorderable types")
		if type(other) == type(self):
			return self.rank() >= other.rank()
		elif type(ohter) == type(0):
			return self.rank() >= other

	def __lt__(self,other):
		if type(other) not in (type(self), type(0)):
			raise TypeError("unorderable types")
		if type(other) == type(self):
			return self.rank() < other.rank()
		elif type(ohter) == type(0):
			return self.rank() < other

	def __le__(self,other):
		if type(other) not in (type(self), type(0)):
			raise TypeError("unorderable types")
		if type(other) == type(self):
			return self.rank() <= other.rank()
		elif type(ohter) == type(0):
			return self.rank() <= other

	def __str__(self):
		return str(self._ranks[self._rank]) + " of " + str(self._suites[self._suite])

A = Card(rank='J',suite='Hearts')
B = Card(rank='Q',suite='Hearts')
print(A > '5')