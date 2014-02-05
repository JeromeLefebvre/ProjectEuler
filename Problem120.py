
# Problem 120


# Did it in the morning and was too drowsy to remember the meaning of mod.. a**3 mod 2 is 0, not a**1.
# so brute force won the day
# http://blog.dreamshire.com/2012/04/26/project-euler-problem-120-solution/
# Talks about smarter solutions

MAX = 1500
# Tested up to n = 3000, but N = 1500 seemed sufficient
def rmax(a,N=MAX):
	max = 0
	for n in range(1,N):
		r = ((a-1)**n + (a+1)**n) % a**2
		if r > max: max = r
	return max

print(sum([rmax(a) for a in range(3,1001)]))

#for i in range(3,1001):
#	if rmax(i) != rmax(i,MAX*2):
#		print(i)