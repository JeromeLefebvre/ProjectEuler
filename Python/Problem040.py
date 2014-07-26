
'''
Problem 40
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''

def problem40():
    Champernowne = ''.join([str(i) for i in range(1, 200000)])
    return int(Champernowne[0])*int(Champernowne[9])*int(Champernowne[99])*int(Champernowne[999])*int(Champernowne[9999])*int(Champernowne[99999])

from cProfile import run
if __name__ == "__main__":
    print(problem40())
    print(problem40() == 210)
    run("problem40()")
