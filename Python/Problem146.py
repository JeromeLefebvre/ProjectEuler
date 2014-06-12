#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=146
Investigating a Prime Pattern
Problem 146
'''

'''
Notes on problem 146():
'''
from PE_primes import isPrime, primesUpTo

'''10
315410
927070
2525870
8146100
16755190
39313460'''


def problem146():
    total = 0
    # n % 210 = 10
    for n in range(10, 15 * 10 ** 7, 210):
        if all([isPrime(n ** 2 + i) for i in [1, 3, 7, 9, 13, 27]]):
            print(n)
            total += n
    # n % 210 = 80
    for n in range(80, 15 * 10 ** 7, 210):
        if all([isPrime(n ** 2 + i) for i in [1, 3, 7, 9, 13, 27]]):
            print(n)
            total += n
    # n % 210 = 130
    for n in range(130, 15 * 10 ** 7, 210):
        if all([isPrime(n ** 2 + i) for i in [1, 3, 7, 9, 13, 27]]):
            print(n)
            total += n
    # n % 210 = 200
    for n in range(200, 15 * 10 ** 7, 210):
        if all([isPrime(n ** 2 + i) for i in [1, 3, 7, 9, 13, 27]]):
            print(n)
            total += n
    return total


'''
long limit = 150000000;
long result = 0;
 
for (long i = 10; i <= limit; i+=10) {
 
    long squared = i * i;
 
    if (squared % 3 != 1) continue;
    if (squared % 7 != 2 && squared % 7 != 3) continue;
 
    if (squared % 9 == 0 ||
        squared % 13 == 0 ||
        squared % 27 == 0)
        continue;
 
    if (IsProbablePrime(squared + 1)  &&
        IsProbablePrime(squared + 3) &&
        IsProbablePrime(squared + 7) &&
        IsProbablePrime(squared + 9) &&
        IsProbablePrime(squared + 13) &&
        IsProbablePrime(squared + 27) &&
       !IsProbablePrime(squared + 19) &&
       !IsProbablePrime(squared + 21))
        result += i;
 
}
'''


def problem146():
    total = 0 
    for i in range(10, 150000000 + 1, 10):
        n = i ** 2
        if n % 3 != 1:
            continue
        if n % 7 != 2 and n % 7 != 3:
            continue
        if n % 9 == 0 or n % 13 == 0 or n % 27 == 0:
            continue
        if all(isPrime(n + j) for j in [1, 3, 7, 9, 13, 27]) and not any(isPrime(n + j) for j in [19, 21]):
            print(i)
            total += i
    return total

if __name__ == "__main__":
    print(problem146())
