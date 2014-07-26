
'''
Problem 33
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

from fractions import gcd

from pe.basic import product

# Using that not 0 == 1 and not 1 == 0
def easyFraction(a, b):
    for x, y in ((0, 0), (1, 0), (0, 1), (1, 1)):
        if str(a)[x] == str(b)[y]:
            if a / b == int(str(a)[not x]) / int(str(b)[not y]):
                return True
    return False

def problem33():
    # a/b
    found = []
    for a in range(10, 100):
        for b in range(a + 1, 100):
            if not b % 10 == 0 and easyFraction(a, b):
                found.append((a, b))
    a = product([d[0] for d in found])
    b = product([d[1] for d in found])
    return b // gcd(a, b)

from cProfile import run
if __name__ == "__main__":
    print(problem33() == 100)
    run("problem33()")
