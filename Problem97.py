
'''
Problem 97
The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form 26972593−1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2p−1, have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×27830457+1.

Find the last ten digits of this prime numbe
'''

# 28433*2**7830457
lastDigits = 28433 % 10**10
for i in range(1,7830457+1):
	lastDigits *= 2
	lastDigits = lastDigits % 10**10

print(lastDigits+1)