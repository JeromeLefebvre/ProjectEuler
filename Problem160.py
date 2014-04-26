
'''
http://projecteuler.net/problem=160
Factorial trailing digits
Problem 160
'''

'''
Notes on problem 160():
'''

from PE_basic import product


def f(n):
	''' Returns the last 5 trailing non-zero digits of n!'''
    if n == 0:
        return 1
    r = product(5 * (n // 5) + i + 1 for i in range(n % 5))
    r *= pow(12, n // 5, 10 ** 5) * f(n // 5)
    while r % 10 == 0:
        r //= 10
    return r % 10 ** 5


def problem160():
    return f(10 ** 12)


from cProfile import run
if __name__ == "__main__":
    # run("problem160()")
    print(problem160() == 16576)
