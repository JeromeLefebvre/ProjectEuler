
'''
Problem 60

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
'''
from PE_primes import isPrime,iPrime

def remarkable(p,q):
	return isPrime(int(str(q) + str(p))) and isPrime(int(str(p) + str(q)))

def problem60():
	primes = [3,7]
	primeGen = iPrime()
	next(primeGen); next(primeGen); next(primeGen); next(primeGen) # 2 and 5 are primes that will never concatinate
	concatenate = {2:set(),3:set(),5:set(),7:{3}}
	def concatenateWith(a):
		concatenate[a] = {p for p in primes[:-1] if remarkable(a,p)}
		return concatenate[a]
	for a in primeGen:
		primes.append(a)
		A = concatenateWith(a)
		for b in A:
			B = concatenate[b] & A
			for c in B:
				C = concatenate[c] & B
				for d in C:
					D = concatenate[d] & C
					for e in D:
						return sum([a,b,c,d,e])

#[8389, 6733, 5701, 5197, 13]
from cProfile import run
if __name__ == "__main__":
	run("problem60()")
	print(problem60() == 26033)