
'''
Problem 50
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

from itertools import accumulate, count

from pe.primes import primesUpTo, isPrime

def problem50():	
	GOAL = 10**6
	listOfPrimes = primesUpTo(GOAL)
	recordLength = 21
	maxPrime = 953
	for index in count():
		for length, running in enumerate(accumulate(listOfPrimes[index:])):
			if length + 1 > recordLength and isPrime(running):
				recordLength = length + 1
				maxPrime = running
			if running > GOAL:
				break
		# If there is no hope, break out
		if sum(listOfPrimes[index: index+recordLength]) > GOAL:
			break
	return maxPrime


if __name__ == "__main__":
	print(problem50() == 997651)
	from cProfile import run
	run("problem50()")

