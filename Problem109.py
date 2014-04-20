#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=109
Darts
Problem 109
'''

'''
Notes on problem 109():
'''
from itertools import combinations_with_replacement


def totaling(*darts):  # 0.102
    return sum(a[0] * a[1] for a in darts)


def totaling(*darts):  # 0.084 seconds
    return sum([a[0] * a[1] for a in darts])


def totaling(*darts):  # 0.048 seconds
    total = 0
    for a in darts:
        total += a[0] * a[1]
    return total


def problem109():
    positions = tuple((i, j) for i in (1, 2, 3)
                      for j in range(1, 21)) + ((1, 25), (2, 25))
    doubles = tuple((2, j) for j in range(1, 21)) + ((2, 25),)

    found = 0
    # Took 3 tries
    for (a, b) in combinations_with_replacement(positions, 2):
        for c in doubles:
            if totaling(a, b, c) <= 99:
                found += 1
    # Took 2 tries
    for b in positions:
        for c in doubles:
            if totaling(b, c) <= 99:
                found += 1
    # Takes one try
    for c in doubles:
        if totaling(c) <= 99:
            found += 1

    return found

from cProfile import run
if __name__ == "__main__":
    run("problem109()")
    print(problem109())
