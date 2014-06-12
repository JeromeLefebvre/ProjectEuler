#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=196
Prime triplets
Problem 196

'''

'''
Notes on problem 196():
'''

from PE_primes import isPrime

def a(n, m):
    if m < 1:
        return 1
    if m > n + 1:
        return 1
    return (n - 1) * (n) // 2 + m

def primesInNbd(n, m):
    # Check the top and bottom row as the elements left and right cannot be primes
    # n,m is a prime number
    locations = []
    for j in [-1, 1]:
        for i in [-1, 0, 1]:
            if isPrime(a(n + j, m + i)):
                locations.append((n + j, m + i))
    return locations


def isPrimeTriplet(n, m):
    locations = primesInNbd(n, m)
    if len(locations) >= 2:
        return True
    for location in locations:
        if len(primesInNbd(*location)) >= 2:
            return True

def S(n):
    total = 0
    previousIsPrime = False # A small optimization that doesn't do much
    for m in range(1, n + 1):
        if previousIsPrime:
            previousIsPrime = False
            continue
        if isPrime(a(n, m)):
            previousIsPrime = True
            if isPrimeTriplet(n, m):
                total += a(n, m)
    return total


def problem196():
    return S(5678027) + S(7208785)

from cProfile import run
if __name__ == "__main__":
    #run("problem196()")
    print(problem196() == 322303240771079935)  # 266
