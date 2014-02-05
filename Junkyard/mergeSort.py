def merge(A,B):
	A.reverse(), B.reverse()
	while A != [] and B != []:
		if A[-1] >= B[-1]:
			yield B.pop()
		else:
			yield A.pop()
	while A != []:
		yield A.pop()
	while B != []:
		yield B.pop()

def mergeSort(L):
	if len(L) <= 2:
		if L[0] <= L[-1]:
			return L
		L.reverse()
		return L
	return [a for a in merge(mergeSort(L[:len(L)//2]),mergeSort(L[len(L)//2:]))]