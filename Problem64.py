

#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=64()
Odd period square roots
Problem 64
All square roots are periodic when written as continued fractions and can be written in the form:

If we continue we would get the following expansion:

The process can be summarised as follows:

It can be seen that the sequence is repeating. For conciseness, we use the notation √23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats indefinitely.

The first ten continued fraction representations of (irrational) square roots are:

√2=[1;(2)], period=1
√3=[1;(1,2)], period=2
√5=[2;(4)], period=1
√6=[2;(2,4)], period=2
√7=[2;(1,1,1,4)], period=4
√8=[2;(1,4)], period=2
√10=[3;(6)], period=1
√11=[3;(3,6)], period=2
√12= [3;(2,6)], period=2
√13=[3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N ≤ 13, have an odd period.

How many continued fractions for N ≤ 10000 have an odd period?
'''

'''
Notes on problem 64():
The main algorirthm is taken from:
http://eli.thegreenplace.net/2009/06/19/project-euler-problem-66-and-continued-fractions/
I have no patience for continued fractions
'''


import math
from projectEuler import isSquare as is_square
def CF_of_sqrt(n):
    """ Compute the continued fraction representation of the
        square root of N.

        The first element in the returned array is the whole
        part of the fraction. The others are the denominators
        up to (and not including) the point where it starts
        repeating.

        Uses the algorithm explained here:
        http://www.mcs.surrey.ac.uk/Personal/R.Knott/Fibonacci/cfINTRO.html
        In the section named: "Methods of finding continued
        fractions for square roots"
    """
    if is_square(n):
        return [int(math.sqrt(n))]

    ans = []

    step1_num = 0
    step1_denom = 1

    while True:
        nextn = int((math.floor(math.sqrt(n)) + step1_num) / step1_denom)
        ans.append(int(nextn))

        step2_num = step1_denom
        step2_denom = step1_num - step1_denom * nextn

        step3_denom = (n - step2_denom ** 2) / step2_num
        step3_num = -step2_denom

        if step3_denom == 1:
            ans.append(ans[0] * 2)
            break

        step1_num, step1_denom = step3_num, step3_denom

    return ans

def problem64():
	hasOddPeriod = 0
	for n in range(1,10000):
		if len(CF_of_sqrt(n)) % 2 == 0:
			hasOddPeriod += 1
	return hasOddPeriod

from cProfile import run
if __name__ == "__main__":
    print(problem64() == 1322)
    run("problem64()")