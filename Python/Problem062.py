#!/usr/local/bin/python3.3

'''
Problem 62
The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''

'''
Notes on problem 62():
'''
from itertools import permutations, count

from pe.sequences import iCube

def problem62():
    length = 0
    cubesOfInterest = {}
    for cube in count(1):
        cube = cube ** 3
        digits = tuple(sorted([a for a in str(cube)]))
        # The idea is we add all cubes in cubesOfInterest
        # Once we hit a new length for cube we check all possible 5 permutations of possible cubes
        # and check if they are all permutations of each other
        if len(digits) > length:
            # Since dictionaries entry aren't sorted, we could hit multiple
            # pairs
            candidates = []
            for c in cubesOfInterest:
                if len(cubesOfInterest[c]) == 5:
                    candidates.append(min(cubesOfInterest[c]))
            if candidates != []:
                return min(candidates)
            length += 1
            cubesOfInterest = {}
        if digits in cubesOfInterest:
            cubesOfInterest[digits].append(cube)
        else:
            cubesOfInterest[digits] = [cube]


from cProfile import run
if __name__ == "__main__":
    print(problem62() == 127035954683)
    run("problem62()")
