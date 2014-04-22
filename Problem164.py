'''
http://projecteuler.net/problem=164
Numbers for which no three consecutive digits have a sum greater than a given value
Problem 164
'''

'''
Notes on problem 164():
Easy dynamic programing + memoization.
'''

from functools import lru_cache


def problem164():
    @lru_cache(maxsize=200)
    def search(digits, n1, n0):
        if digits == 20:
            return 1
        total = 0
        for i in range(10 - n0 - n1):
            total += search(digits + 1, n0, i)
        return total
    return sum([search(1, 0, i) for i in range(1, 10)])  # leading digits

# 378158756814587
from cProfile import run
if __name__ == "__main__":
    # run("problem164()")
    print(problem164())
