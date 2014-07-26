
'''
Problem 31
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''

# There should be a cleaner recursive function


def problem31():
    # aL1 + b50p + c20p + d10p + e5p + f2p + g1p
    # start with 1*L2 = L2
    total = 1
    for a in range(0, 200 // 100 + 1):
        for b in range(0, (200 - 100 * a) // 50 + 1):
            for c in range(0, (200 - 100 * a - 50 * b) // 20 + 1):
                for d in range(0, (200 - 100 * a - 50 * b - 20 * c) // 10 + 1):
                    for e in range(0, (200 - 100 * a - 50 * b - 20 * c - 10 * d) // 5 + 1):
                        for f in range(0, (200 - 100 * a - 50 * b - 20 * c - 10 * d - 5 * e) // 2 + 1):
                            f = 200 - 2 * f - 5 * e - \
                                10 * d - 20 * c - 50 * b - 100 * a
                            total += 1
    return total

if __name__ == "__main__":
    print(problem31() == 73682)
    from cProfile import run
    run("problem31()")
