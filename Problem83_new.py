


data = '''131	673	234	103	18
201	96	342	965	150
630	803	746	422	111
537	699	497	121	956
805	732	524	37	331'''
# Some large value
MAX = 1000000
A = [[int(a) for a in l.split('\t')] for l in data.split('\n')]
length = len(A[0])
B = [[MAX for j in range(0,length+2)] for i in range(0,length+2)]
B[1][1] = A[0][0]
import copy
previous = MAX+1
while B[-2][-2] != previous:
	C,previous = copy.copy(B),B[-2][-2]
	for i in range(1,length+1):
		for j in range(1,length+1):
			if not(i == 1 and j == 1):
				B[i][j] = A[i-1][j-1] + min(C[i-1][j],C[i][j-1],C[i+1][j],C[i][j+1])
print(B[-2][-2])