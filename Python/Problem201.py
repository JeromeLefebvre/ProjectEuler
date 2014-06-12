'''
http://projecteuler.net/problem=201
Subsets with a unique sum
Problem 201
'''

'''
Notes on problem 201():
'''
from collections import defaultdict


def naive(n, m):
    A = [i ** 2 for i in range(1, n + 1)]
    uniquesums = set()
    badsums = set()
    for s in combinations(A, m):
        ss = sum(s)
        if ss in uniquesums:
            uniquesums.remove(ss)
            badsums.add(ss)
        elif ss not in badsums:
            uniquesums.add(ss)
    return sum(uniquesums), max(uniquesums)


def problem201():
    partialSums = [defaultdict(int) for i in range(51)]
    partialSums[0][0] = 1  # i.e. 0 can be reached with a sum of 0 elements

    # Go over each integer once
    for i in range(1, 101):
    	# You can reach 50 levels in total
        for numberOfSummands in range(49, max(-1, i - 52), -1):
        	# For all the sums that could be reached, you get one more
            for k in partialSums[numberOfSummands]:
                z = k + i ** 2
                partialSums[numberOfSummands + 1][z] += partialSums[numberOfSummands][k]

    total = 0
    for n in partialSums[50]:
        if partialSums[50][i] == 1:
            total += i
    return total

from cProfile import run
if __name__ == "__main__":
    # run("problem201()")
    print(problem201() == 115039000)
