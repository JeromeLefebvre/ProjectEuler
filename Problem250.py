'''
http://projecteuler.net/problem=250
250250
Problem 250
'''

'''
Notes on problem 250():
x^x mod 250 is a periodic function
to see that note that (x+n)^(x+n) = (x+n)^x (x+n)^n
and if 250|n and 100=\phi(250)|n then the period divides n.
So, in particular the period divides 500. We could use this to speed things up.
'''

from collections import defaultdict
from functools import lru_cache

# Sadly, noting that the function is periodic does not seem to speed up the calculations.
@lru_cache(maxsize=1000)
def f(x):
	return pow(x, x, 250)

def problem250():
    equivalances = defaultdict(int)

    for i in range(1, 250250 + 1):
        if i % 500 == 0:
            equivalances[0] += 1
        else:
            equivalances[f(i%500)] += 1

    # We find all possible sums
    sums = [1] + [0] * 249 
    for index in range(250):
        for j in range(equivalances[index]):
            sums = [(sums[k] + sums[k - index]) % 10 ** 16 for k in range(250)]

    return sums[0] - 1

from cProfile import run
if __name__ == "__main__":
    #run("problem250()")
    print(problem250() == 1425480602091519)
