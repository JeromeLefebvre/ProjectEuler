
# Problem 46
# The number was much smaller than I though: 5777
from primes import rwh_primes2

def isSquare(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

def problem46():
	primesList = rwh_primes2(10**4)
	for l in range(1,10**4):
		n = 2*l + 1
		flag = True
		if not (n in primesList):
			a = 1
			while 2*a**2 < n:
				q = n - 2*a**2
				if q in primesList:
					flag = False
					break
				a += 1
		else:
			flag = False
		if flag:
			return n

from cProfile import run
if __name__ == "__main__":
	print(problem46() == 5777)
	run("problem46()")

