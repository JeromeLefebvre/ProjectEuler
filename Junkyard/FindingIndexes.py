
import timeit
from projectEuler import rwh_primes2

def containsSorted(l,n):
	print(l)
	if l == [] or (len(l) <= 2 and l[0] != n and l[-1] != n):
		return False	
	elif l[0] == n or l[1] == n:
		return True
	return containsSorted(l[1:len(l)//2],n) or containsSorted(l[len(l)//2:-1],n)

containsSorted(primes,3)

def largestBelow(l,n):
	if n in l:
		return n
	return l[largestIndexBelow(l,n)-1]

def largestIndexBelow(l,n):
	if l == [] or n <= l[0]:
		return 0
	if n > l[-1]:
		return len(l) 
	return largestIndexBelow(l[:len(l)//2],n) + largestIndexBelow(l[len(l)//2:],n)


def largestBelowA(l,n):
	if n in l:
		return n
	return l[largestIndexBelow(l,n)-1]

def largestIndexBelowA(l,n):
	if l == [] or n <= l[0]:
		return 0
	if n > l[-1]:
		return len(l) 
	return largestIndexBelow(l[:len(l)//2],n) + largestIndexBelow(l[len(l)//2:],n)


def largestBelowSlow(l,n):
	for index,a in enumerate(l):
		if a > n:
			return l[index -1]
		if a == n:
			return a

primes = rwh_primes2(20)
print(largestBelow(primes,5))


tests = [(2,2),(3,3),(4,3),(5,5),(6,5)]
for test in tests[:4]:
	#print("*"*100)
	print(test[0], test[1])
	print(largestBelow(primes,test[0]) == test[1],largestBelow(primes,test[0]))

'''
import random
for i in range(1,1000):
	d = random.randint(2,2000)
	if largestBelow(primes,d) != largestBelowA(primes,d):
		print(largestBelow(primes,d), largestBelowA(primes,d),d)
'''