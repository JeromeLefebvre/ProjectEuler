
'''
Problem 56
A googol (10100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
'''

from itertools import permutations

from pe.digits import applyToDigits


def problem56():
    # As a and b increase, the number of digits of a**b increase and thus the
    # sum of digits will also likely increase.
    # For example 90**90 has 176 digits, so a number around it should have a digit sum of around 5*176
    # And it keeps increasing from there.
    return max(applyToDigits(a ** b, lambda x: x) for a, b in permutations(range(90, 100), 2))

if __name__ == "__main__":
    print(problem56() == 972)
    from cProfile import run
    run("problem56()")
