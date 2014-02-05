
#!/usr/local/bin/python3.3

'''
http://projecteuler.net/problem=149
Searching for a maximum-sum subsequence.
Problem 149
Looking at the table below, it is easy to verify that the maximum possible sum of adjacent numbers in any direction (horizontal, vertical, diagonal or anti-diagonal) is 16 (= 8 + 7 + 1).

−2	5	3	2
9	−6	5	1
3	2	7	3
−1	8	−4	  8
Now, let us repeat the search, but on a much larger scale:

First, generate four million pseudo-random numbers using a specific form of what is known as a "Lagged Fibonacci Generator":

For 1 ≤ k ≤ 55, sk = [100003 − 200003k + 300007k3] (modulo 1000000) − 500000.
For 56 ≤ k ≤ 4000000, sk = [sk−24 + sk−55 + 1000000] (modulo 1000000) − 500000.

Thus, s10 = −393027 and s100 = 86613.

The terms of s are then arranged in a 2000×2000 table, using the first 2000 numbers to fill the first row (sequentially), the next 2000 numbers to fill the second row, and so on.

Finally, find the greatest sum of (any number of) adjacent entries in any direction (horizontal, vertical, diagonal or anti-diagonal).
'''

'''
Notes on problem 149():
I just got lucky and solved it by simply having checked all rows and columns
No diagonals
'''
from projectEuler import primes

def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def s(k,_d={}):
	if k in _d:
		return _d[k]
	if k <= 55:
		_d[k] = (100003 - 200003*k + 300007*k**3)% 1000000 - 500000
		return _d[k] 
	if k <= 4000000:
		_d[k] = (s(k-24) + s(k-55) + 1000000) % 1000000 - 500000
		return _d[k] 
	print("FUCK")
def problem149():
	record = 52852124
	# Checking each rows
	for l in range(0,2000):
		m = max_subarray( [s(k) for k in range(1 + 2000*l,2001 + 2000*l) ] )
		if m > record:
			record = m
	# Checking each columns
	for c in range(1,2000):
		m = max_subarray( [s(c+2000*k) for k in range(0,2000) ] )
		if m > record:
			record = m	
	return record


if __name__ == "__main__":
	print(problem149())
 