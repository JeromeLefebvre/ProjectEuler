#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=156
Counting Digits
Problem 156
'''

'''
Notes on problem 156():
'''


def f(n, digit):
    count = 0
    factor = 1
    i = 1
    while n // factor != 0:
        lower_number = n - (n // factor) * factor
        curr_number = (n // factor) % 10
        higher_number = n // (factor * 10)
        if curr_number < digit:
            count += higher_number * factor
        elif curr_number == digit:
            count += higher_number * factor + lower_number + 1
        else:
            count += (higher_number + 1) * factor
        factor *= 10
        i+=1
    return count


def solve():
    count = 0
    for digit in range(1, 10):
        found = []
        def binary_search(digit, lower=1, upper=10**11):
            if lower + 1 == upper:
                if f(lower, digit) == lower:
                    found.append(lower)
                return
            middle = (lower + upper) // 2
            lower_value = f(lower, digit)
            upper_value = f(upper, digit)
            middle_value = f(middle, digit)
            if middle_value >= lower and middle >= lower_value:
                binary_search(digit, lower, middle)
            if upper_value >= middle and upper >= middle_value:     
                binary_search(digit, middle, upper)
        binary_search(digit)
        count += sum(found)
    return count
                
def problem156():
    return solve()
    
# 21295121502550
from cProfile import run
if __name__ == "__main__":
    # run("problem156()")
    #print(f(199981,1))
    print(problem156() == 21295121502550)
