

'''
Problem 58
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
'''
from itertools import count

from pe.primes import isPrime


def problem58():
    primes = 0
    for shell in count(1):
        # We only need to check the 4 cornes and there is an easy formula to
        # generate all of them
        primes += sum(1 for i in range(1, 4)
                      if isPrime((2 * shell + 1) ** 2 - 2 * i * shell))
        if primes / (4 * shell + 1) < 0.10:
            return 2 * shell + 1

if __name__ == "__main__":
    print(problem58() == 26241)
    from cProfile import run
    run("problem58()")
