#!/usr/local/bin/python3.4.1

'''
http://projecteuler.net/problem=36
Double-base palindromes
Problem 36
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

from itertools import combinations_with_replacement, permutations

from pe.digits import numberFromlist
from pe.sequences import isBinaryPalindrome

def problem36():
    seen = set()
    for n in range(1, 4):
        for c in combinations_with_replacement(range(0, 10), n):
            for d in permutations(c, n):
                m = numberFromlist(d + d[::-1])
                if isBinaryPalindrome(m):
                    seen.add(m)
                m = numberFromlist(d[:-1] + d[::-1])
                if isBinaryPalindrome(m):
                    seen.add(m)
    return sum(seen)

from cProfile import run
if __name__ == "__main__":
    print(problem36() == 872187)
    run("problem36()")
