#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=107
Minimal network
Problem 107
'''

#Notes on problem 107():

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

samplenetwork = {}
for r in range(0,7):
	for c in range(r,7):
		# if we have a entry, then we have a matrix
		if samplematrix[r][c] != '-':
			samplenetwork[(indices[r],indices[c])]  = int(samplematrix[r][c])



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

def canRemove(graph,node):
	
def findMin(network):
	graph = [key for key in samplenetwork]
	return 
graph = [key for key in samplenetwork]
print(isConnected(graph))

def problem107():
	pass


from cProfile import run
if __name__ == "__main__":
	run("problem107()")
	print(problem107())
	
 
 