

'''
Problem 28
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''


def problem28():
    GOAL = 1001
    total = 0
    for shell in range(1, (GOAL - 1) // 2 + 1):
        for i in range(0, 4):
            total += (2 * shell + 1) ** 2 - 2 * i * shell
    return total + 1

if __name__ == "__main__":
    print(problem28() == 669171001)
    from cProfile import run
    run("problem28()")
