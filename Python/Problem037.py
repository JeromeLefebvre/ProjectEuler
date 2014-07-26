
'''
Problem 37
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

from pe.digits import numberOfDigits


def rightTruncates(q):
    ''' rightTruncates(int) -> iterator  yield all the right truncates of a number, e.g. 123 returns 23, 3
    but 101 returns only 1'''
    while q > 9:
        # need to recompute the number of digits in case on contained 0
        q %= 10 ** (numberOfDigits(q) - 1)
        yield q


def leftTruncates(q):
    '''leftTruncates(int) -> iterator -- Yields all the left truncates of a number'''
    while q > 9:
        q //= 10
        yield q


def isMadeOfOddOrWithLeading2(n):
    '''isMadeOfOddOrWithLeading2(int) -> bool -- Checks if a number is made of the form abcd with b,c,d odd numbers and a odd number or 2'''
    while n > 10:
        if not n % 10 in {1, 3, 7, 9}:
            return False
        n //= 10
    return n % 10 in {1, 2, 3, 5, 7, 9}

from pe.primes import iPrime


def problem37():
    found = set()
    primes = iPrime()
    # The primes 2,3,5,7 are not candidates, but they could be the result of a
    # truncation.
    primesOfInterest = {next(primes), next(primes), next(primes), next(primes)}
    for q in primes:
        if isMadeOfOddOrWithLeading2(q):
            primesOfInterest.add(q)
            if all(p in primesOfInterest for p in leftTruncates(q)) and all(p in primesOfInterest for p in rightTruncates(q)):
                found.add(q)
                if len(found) > 10:
                    return sum(found)

import cProfile
if __name__ == "__main__":
    print(problem37() == 748317)
    cProfile.run("problem37()")
