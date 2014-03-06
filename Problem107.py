#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=107
Minimal network
Problem 107
'''

#Notes on problem 107():

def attachedTo(graph,node):
	return { k[1] for k in graph if k[0] == node }.union({k[0] for k in graph if k[1] == node})

def isConnected(graph):
	indices = ['a','b','c','d','e','f','g']
	seen = ['a']
	tovisit = attachedTo(graph,'a')
	while len(tovisit) != 0:
		v = tovisit.pop()
		seen.append(v)
		tovisit = tovisit.union(attachedTo(graph,v))
		tovisit = tovisit.difference(seen)
	return sorted(seen) == indices

from random import sample
def found(graph):
	initial = sample(graph)
	seen = [initial[0]]
	tovisit = attachedTo(graph,initial[0])
	while len(tovisit) != 0:
		v = tovisit.pop()
		seen.append(v)
		tovisit = tovisit.union(attachedTo(graph,v))
		tovisit = tovisit.difference(seen)

def findMin(d):
	return min(d,key=d.get)

def addsNothing(graph, vertex):
	# Returns true if both the head and tail are already in the graph
	head = vertex[0]
	tail = vertex[1]
	foundHead, foundTail = False, False
	for k in graph:
		if head in k:
			foundHead = True
		if tail in k:
			foundTail = True
		if foundTail and foundHead:
			return True
	return False

def problem107():
	seen = set()
	i = 0
	while not isConnected(seen):
		i += 1
		if i >= 20: break
		candidate = findMin(samplenetwork)
		print(candidate)
		# If this doesn't contribute to anything, skip this node
		if addsNothing(seen, candidate):
			samplenetwork.pop(candidate)
		else:
			samplenetwork.pop(candidate)
			seen.add(candidate)
		print(seen)
	return seen


class Line():
	def __init__(self,nodes,weight):
		self.nodes = nodes
		self.weight = weight

class Graph():
	def __init__(self,nodes,lines):
		self.nodes = nodes
		self.lines = lines

	def append(self,line):
		self.lines.append(line)

	@classmethod
	def canReachFrom(cls,node,lines):
		'''Returns a list of all the nodes that can be reach starting from the given node'''
		return { k[1] for k in lines if k[0] == node }.union({k[0] for k in lines if k[1] == node})

	@classmethod
	def connectedSubgraphs(cls,lines):
		'''Returns a set of nodes for each connected subgraph'''
		forests = []
		for l in lines:
			subgraph = canReachFrom(l)
			if l not in forests:
				forests.append(subgraph)
		return forests

	@classmethod
	def isConnected(cls,lines):
		return len(connectedSubgraphs(lines)) == 1

	def linesInOrder(self):
		sorted(d,key=d.get)

def problem107():
	SamepleData = '''-	16	12	21	-	-	-
	16	-	-	17	20	-	-
	12	-	-	28	-	31	-
	21	17	28	-	18	19	23
	-	20	-	18	-	-	11
	-	-	31	19	-	-	27
	-	-	-	23	11	27	-'''

	samplematrix = [['-' for i in range(0,7)] for j in range(0,7)]
	for r, row in enumerate(SamepleData.split('\n')):
		for c, col in enumerate(row.split('\t')):
			samplematrix[r][c] = col

	indices = ['a','b','c','d','e','f','g']

	graph = Graph(indices,[])

	for r in range(0,7):
		for c in range(r,7):
			# if we have a entry, then we have a matrix
			if samplematrix[r][c] != '-':
				node = Line((indices[r],indices[c]), int(samplematrix[r][c]))
				samplenetwork[(indices[r],indices[c])]  = int(samplematrix[r][c])

from cProfile import run
if __name__ == "__main__":


	#run("problem107()")

	print(problem107())
	
 
 