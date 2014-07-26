
# Problem 46
# The number was much smaller than I though: 5777
from pe.primes import primesUpTo
from pe.quadratics import isSquare


def problem46():
    primesList = primesUpTo(10 ** 4)
    for l in range(1, 10 ** 4):
        n = 2 * l + 1
        flag = True
        if not (n in primesList):
            a = 1
            while 2 * a ** 2 < n:
                q = n - 2 * a ** 2
                if q in primesList:
                    flag = False
                    break
                a += 1
        else:
            flag = False
        if flag:
            return n

if __name__ == "__main__":
    print(problem46() == 5777)
    from cProfile import run
    run("problem46()")
