#!/usr/local/bin/python3.3

'''
Problem 51
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
'''

'''
If we consider the set set of candidates mod 3, that the only way that the set of prime contains 8 elements
is if there is multiple of 3 replacements that have to tbe done.
Furthermore, if we are looking for the smallest element, then the digit to replace has to be 0,1,2.
'''

from pe.primes import isPrime, primesUpTo


def primes8(m, i):
    def primeCheck(i,s):
        return isPrime(int(m.replace(i, s)))
    digits = [str(i) for i in range(0,10)]
    return len([s for s in digits if m.replace(i, s)[0] != '0' and primeCheck(i,s)]) == 8


def problem51():
    primes = primesUpTo(10 ** 7)
    for p in primes[1229:]:
        m = str(p)
        for i in ['0', '1', '2']:
            if m.count(i) == 3 and primes8(m, i):
                return p

if __name__ == "__main__":
    print(problem51() == 121313)
    from cProfile import run
    run("problem51()")
