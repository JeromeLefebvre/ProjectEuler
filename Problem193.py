
# Problem 193
from operator import mul
from functools import reduce
from primes import rwh_primes2, gen_primes
from itertools import combinations

def prod(args):
	return reduce(mul,args)

import itertools
def erat2( ):
    D = {  }
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x&1):
                x += p
            D[x] = p
            
GOAL = 2**50

listOfPrimes = []
for p in gen_primes():
	if p < GOAL:
		listOfPrimes.append(p)
	else:
		break

maxTau = 1
while True:
	if prod(listOfPrimes[0:maxTau + 1]) < GOAL:
		maxTau += 1
	else:
		break

count = 0
for lengthOfTuples in range(1,maxTau+1):
	for c in combinations(listOfPrimes,lengthOfTuples):
		if prod(c) < GOAL:
			print(c)
			count += 1

# The plus 1 is to account for 1
print(count+1)