
'''
Problem 50
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

from PE_primes import primesUpTo, isPrime

def problem50a():
	GOAL = 10**6
	listOfPrimes = primesUpTo(GOAL)
	knowMinLengths = 21
	maxLength = 0
	runningSum = 0
	# checking how long the maximum chain can be
	for a in listOfPrimes:
		runningSum += a
		if runningSum > GOAL:
			break
		maxLength += 1
	record = 0
	for l in range(knowMinLengths,maxLength):
		for j in range(0,len(listOfPrimes) - l):
			s = sum([listOfPrimes[a] for a in range(j, j+l+1)])
			if s > GOAL:
				break
			if s > record and s in listOfPrimes:
				record = s
				break
	return record


def problem50():
	GOAL = 10**6
	listOfPrimes = primesUpTo(GOAL)
	recordLength = 21
	maxPrime = 0
	for index, p in enumerate(listOfPrimes):
		running = p
		for length, q in enumerate(listOfPrimes[index+1:]):
			running += q
			if length + 1 > recordLength and running > maxPrime and isPrime(running):
				recordLength = length + 1
				maxPrime = running
			if running > GOAL:
				break
		# If there is no hope, break out
		if sum(listOfPrimes[index: index+recordLength]) > GOAL:
			break
	return maxPrime

def problem50a():
	from itertools import accumulate, count
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


from cProfile import run
if __name__ == "__main__":
	print(problem50() == 997651)
	run("problem50()")
	print(problem50a() == 997651)
	run("problem50a()")

