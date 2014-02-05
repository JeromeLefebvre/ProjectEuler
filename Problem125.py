
# Problem 125


GOAL = 10**8
# lazily generating all palidromes
def isPalindrome(s):
    ''' check if a number is a Palindrome '''
    s = str(s)
    return s == s[::-1]

#palidromes = [a for a in range(2,GOAL) if isPalindrome(a)]

foundPalidromes = []
# n stands for the length of chain
for n in range(2,1000):
	j = 1
	a = -1
	while a < GOAL:
		a = sum([i**2 for i in range(j,j+n)])
		if isPalindrome(a) and 1< a < GOAL:
			#print(a,[i for i in range(j,j+n)],[i**2 for i in range(j,j+n)])
			foundPalidromes.append(a)
		j += 1

# Forgot to check for duplicates
print(len(set(foundPalidromes)))
print(sum(set(foundPalidromes)))