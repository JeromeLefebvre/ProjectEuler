#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=381
(prime-k) factorial
Problem 381
'''

'''
Notes on problem 381():
Wilson's theorm takes care of (n-1)!
'''

from math import factorial as f
from PE_primes import isPrime, iPrime

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def factorial(n,modulus):
    product = 1
    for i in range(1,n+1):
        product *= i % modulus
        product %= modulus

    return product % modulus


# 37472
def S(p):
    return ( sum([f(p-k) % p for k in range(2,6)]) % p + (p-1) ) %p

def S(p):
    return sum( [-1 + -1*modinv(p-1,p) + -1*modinv(p-1,p)*modinv(p-2,p) + -1*modinv(p-1,p)*modinv(p-2,p)*modinv(p-3,p) + -1*modinv(p-1,p)*modinv(p-2,p)*modinv(p-3,p)*modinv(p-4,p) ] ) % p

def S(p):
    total = -1
    n = -1
    for k in range(1,5):
        n *= modinv(p-k,p)
        total += n
    return total % p

# 139602943319822
def problem381():        
    total = 0
    for p in iPrime(5):
        if p >= 10**8:
            break
        total += S(p)
    return total


from cProfile import run
if __name__ == "__main__":
    #run("problem381()")
    print(problem381() == 139602943319822) 