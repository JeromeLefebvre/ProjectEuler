
'''
Problem 92
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
'''

GOAL = 10*10**6
numberSeens = {1:False,89:True}

countOf89 = 0
for i in range(1,GOAL):
	if not i in numberSeens.keys():
		listOfIntermediates = [i]
		while not i in numberSeens.keys():
			i = sum([int(a)**2 for a in str(i)])
			listOfIntermediates.append(i)
		for j in listOfIntermediates:
			numberSeens[j] = numberSeens[i]

total = sum([1 for a in numberSeens.keys() if numberSeens[a] and a < GOAL])
print(total)