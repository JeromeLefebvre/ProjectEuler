

'''
Problem 38
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''
from pe.sequences import isPandigitalMultiples


def problem38():
    record = 0
    for a in range(1, 20000):
        for n in range(1, 10):
            if isPandigitalMultiples(a, n):
                d = ''
                for i in range(1, n + 1):
                    d += str(i * a)
                if int(d) > record:
                    record = int(d)
    return record

if __name__ == "__main__":
    print(problem38() == 932718654)
    from cProfile import run
    run("problem38()")
