
'''
Problem 34
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

'''
from itertools import combinations_with_replacement
from math import factorial

from pe.digits import digits


def problem34():
    ''' This is a digit problem so we approach it this way'''
    total = 0
    for n in range(2, 6):
        for c in combinations_with_replacement(range(0, 10), n):
            m = sum([factorial(i) for i in c])
            if sorted(digits(m)) == list(c):
                total += m
    return total


if __name__ == "__main__":
    print(problem34() == 40730)
    from cProfile import run
    run("problem34()")
