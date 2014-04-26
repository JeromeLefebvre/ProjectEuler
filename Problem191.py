'''
http://projecteuler.net/problem=191
Prize Strings
Problem 191
'''

'''
Notes on problem 191():
Combinatorics should be done along the lines of:
http://jsomers.net/blog/project-euler-problem-191-or-how-i-learned-to-stop-counting-and-love-induction

Can't be late twice:
(L,L,*,*,*,...,*) and all it's permutations must be taken out
Can't be Abstent three times in a row
(*,*,A,A,A,*,...,*)
all permutations that keep the 3 A's together
Then remove the intersection of the two.

The naive way can't be improved much.

But, the way to do this is to simplify the naive way until it can be memoize
Which is the final solution.
'''


def problem191():
    def count(sofar=()):
        if sofar.count('L') == 2:
            return 0
        if len(sofar) > 2 and sofar[-3:] == ('A', 'A', 'A'):
            return 0
        if len(sofar) == 4:
            return 1
        total = 0
        for day in ['0', 'A', 'L']:
            total += count(sofar + (day,))
        return total
    return count()


def problem191():
    seen = {}

    def count(days, daysLate, daysAbsent):
        try:
            return seen[(days, daysLate, daysAbsent)]
        except:
            pass
        if daysLate > 1 or daysAbsent >= 3:
            return 0
        if days == 30:
            return 1
        total = 0
        total += count(days + 1, daysLate, 0)  # Regular day
        total += count(days + 1, daysLate, daysAbsent + 1)  # Absent day
        total += count(days + 1, daysLate + 1, 0)  # Late day
        seen[(days, daysLate, daysAbsent)] = total
        return total
    return count(0, 0, 0)


from cProfile import run
if __name__ == "__main__":
    run("problem191()")
    print(problem191() == 1918080160)
