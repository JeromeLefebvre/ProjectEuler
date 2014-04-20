'''
http://projecteuler.net/problem=122
Efficient exponentiation
Problem 122
'''

'''
Notes on problem 122():
'''


def problem122():
    m = {}
    seen = set()

    def gen(current, maximum):
        if maximum > 200:
            return
        if current in seen:
            return
        if maximum not in m:
            m[maximum] = current
        else:
            if len(current) > len(m[maximum]):
                return
            if len(current) < len(m[maximum]):
                m[maximum] = current
        seen.add(current)
        b = max(current)
        for a in current:
            gen(current + (a + b,), max(maximum, a + b))

    gen((1,), 1)

    total = 0
    for n in range(1, 201):
        total += len(m[n]) - 1

    return total


from cProfile import run
if __name__ == "__main__":
    # run("problem122()")
    print(problem122() == 1582)
