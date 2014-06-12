
'''
http://projecteuler.net/problem=160
Factorial trailing digits
Problem 160
'''

'''
Notes on problem 160():
'''

from PE_basic import product

'''
my horribly slow solution, was improved on by what I found on the forum.

This is from the forum:

Define g(n) to be the stripping-of-zeroes/mod-100000 operation on numbers. We will write a ≡g b if the images of a and b under g are the same.

Now, by definition, we know that

(5k+j)! = (5k+j) * ... * (5k+1) * (5k)!

A little observation shows us that 

(5k)! ≡g 5!^k * k!


So our function f(n) is defined recursively:
f(0) = 1
f(n = 5k + j) = g((5k + 1)(5k + 2)...(5k + j) * 12k * f(k))
'''

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
