'''
http://projecteuler.net/problem=128

Notes on problem 128():
'''

from PE_primes import isPrime
def problem128():
    count = 1
    limit = 2000
    n = 0
    number = 0
    while count < limit:
        n += 1
        if (isPrime(6 * n - 1) and isPrime(6 * n + 1) and isPrime(12 * n + 5)):
            count += 1;
            number = (3 * n * n - 3*n + 2)
            if (count >= limit):
                break
        if (isPrime(6 * n + 5) and isPrime(6 * n - 1) and isPrime(12 * n - 7) and n != 1):
            count += 1
            number = (3 * n * n + 3*n + 1)
    return number
    
from cProfile import run
if __name__ == "__main__":
	#run("problem128()")
	print(problem128()) 