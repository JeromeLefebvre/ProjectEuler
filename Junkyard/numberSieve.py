
from projectEuler import product, rwh_primes2

GOAL = 10**7
a = []
for i in range(1,GOAL):
	a.append([1])

for p in rwh_primes2(GOAL):
	[a[i].append(p) for i in range(p,GOAL-1,p)]


