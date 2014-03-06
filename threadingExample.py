from threading import Thread

from PE_primes import iFactorize

import builtins

class mylist(list):
    def __init__(self):
        super().__init__(self)
        self.locked = False

    def append(self,element):
        if not self.locked:
            super().append(element)

builtins.list = mylist

a = list()
a.locked = True
a.append(421)
print(a)
a.locked = False
a.append("fkldja")
print(a)


class PrimeThread(Thread): 
    '''A prime factorization for Fermat primes'''
    def __init__(self, prime,n,factorsSoFar):
        Thread.__init__(self)
        self.prime = prime
        self.n = n
        self.factorsSoFar = factorsSoFar
        self.start()
 
    def run(self):
        for q in iFactorize(self.prime):
            #print("One factor of ", self.n, " is: ", q)
            self.factorsSoFar.append((q,self.n))
            self.factorsSoFar.sort()
            print(self.factorsSoFar[0:15])
        print("the number ", self.n, " has been factorize")
 
def factorizePrimes(primes):
    factorsSoFar = []
    for (p,n) in primes:
        PrimeThread(p,n,factorsSoFar)
        
if __name__ == "__main__":
    factorizePrimes([(2**(2**n)+1,n) for n in range(0,30) ])


'''
[(5, 1), (17, 2), (257, 3), (641, 5), (65537, 4), (114689, 12), (274177, 6), (319489, 11), (974849, 11), (2424833, 9), (6700417, 5), (26017793, 12), (45592577, 10), (63766529, 12), (1214251009, 15)]

I've been trying to come up with a Euler project type of problem. Here is one attempt:

**************
A Fermat number is a number of the form F_n = 2^(2^n) + 1, n >= 0. Amongst the first few numbers, F_0 = 3, F_1 = 5, F_2 = 17, we see that they are prime. But, starting from n = 6, we find that this is no longer the case. We also further have that each number prime factor is unique.

Find the sum of the 15 smallest prime factors of a Fermat number.

**************

A big Caveat: By a computer search, I found lots of "small" factors, but I don't have a proof that my factors are actually the smallest. Simply, I have a quick algorithm that finds those first 15 quickly and then doesn't find anything better after running for several hours.
'''