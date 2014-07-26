
'''
Problem39
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

''' I lost track of the algorithm and not sure why I need the *2 at the end'''

from pe.quadratics import isSquare


def integerSquare(d):
    ''' Expects a square integer '''
    # For some reason, using a power is much faster than calling math.sqrt
    s = int(d ** (1 / 2))
    if d == s ** 2:
        return s
    # Does this ever fail?civ
    print("INTEGER SQUARE WAS NEEDED")
    return s + 1


def problem39():
    GOAL = 1000
    values = {}
    for p in range(1, GOAL + 1):
        values[p] = []
    # the bounds come from a + b > c, a < c, b < c and a + b + c <= 1000
    for a in range(1, GOAL // 2):
        for b in range(1, (500 - a) // 2):
            if isSquare(a ** 2 + b ** 2):
                c = integerSquare(a ** 2 + b ** 2)
                values[a + b + c].append([a, b, c])
    record = 0
    recordp = 0
    for p in range(1, GOAL + 1):
        if len(values[p]) / 2 > record:
            record = len(values[p]) / 2
            recordp = p
    return recordp * 2

if __name__ == "__main__":
    print(problem39() == 840)
    from cProfile import run
    run("problem39()")
