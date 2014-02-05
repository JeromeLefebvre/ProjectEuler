
import random
import unittest
from projectEuler import primes, rwh_primes2,generateFactors,product

'''
class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.c = primes(save=True, initial=False)
        #self.c.cleanup()
    def test_primes(self):
        # make sure the shuffled sequence does not lose any elements
        self.assertEqual(self.c.knowPrimes, [2])
        self.c.addPrime()
        self.assertEqual(self.c.knowPrimes, [2,3])
        self.assertEqual(self.c.currentNumber, 4)
        self.c.addPrimeUpTo(10)
        self.assertEqual(self.c.knowPrimes, [2,3,5,7])
        self.c.addPrime()
        self.assertEqual(self.c.knowPrimes, [2,3,5,7,11])

    
    def test_factors(self):
        self.c.cleanup()
        self.assertEqual(self.c.factors(6),[2,3])
        #should have reached for more primes than needed
        self.assertEqual(self.c.knowPrimes, [2,3])
        self.assertEqual(self.c.factors(7),[7])
        self.assertEqual(self.c.knowPrimes, [2,3,5,7])
        self.assertEqual(self.c.factors(600851475143),[71,839,1471,6857])
        self.assertEqual(self.c.knowPrimes, rwh_primes2(6857+1))

    def test_pi(self):
        self.assertEqual(self.c.indexOfFirstPrimeBelow(6),2)
        self.assertEqual(self.c.knowPrimes[self.c.indexOfFirstPrimeBelow(2*10**6)],1999993)
        self.assertEqual(self.c.pi(10),4)
        self.assertEqual(self.c.pi(10**2),25)
        self.assertEqual(self.c.pi(10**3),168)
        self.assertEqual(self.c.pi(10**4),1229)
        self.assertEqual(self.c.pi(2*10**6),148933)
        #self.assertEqual(self.c.pi(10**7),664579)

    def test_primeRange(self):
        primesTo = rwh_primes2(3*10**7)
        self.assertEqual(self.c[10:20],[11,13,17,19])
        start,stop = 0,2*10**6
        primesToTest = []
        for p in primesTo:
            if start <= p <= stop:
                primesToTest.append(p)
            if p > stop:
                break
        self.assertEqual(self.c[0:2*10**6],primesToTest)
    
    def test_generate(self):
        seen = []
        for c in generateFactors(100,self.c):
            seen.append(product(c))
        seen.sort()
        self.assertEqual(seen,[i for i in range(2,100+1)])

    def test_phi(self):
        self.assertEqual(self.c.phi(3213),1728)
        self.assertEqual(self.c.phi(421),420)
        self.assertEqual(self.c.phi(42135321),28090212)
        self.assertEqual(self.c.phi(854),360)
'''

from projectEuler import solveIntegerQuadratic, solveIntegerLinear, isTriangle
class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        pass
    def test_solving(self):
        # (x + a)(x + b) = x**2 + (a+b)x + ab
        for a in range(-100,100):
            for b in range(-100,100):
                solns = [-a,-b]
                solns.sort()
                self.assertEqual(solveIntegerQuadratic(1,a+b,a*b),solns)
        # x**2 + 1 = 0 has no solutions
        self.assertEqual(solveIntegerQuadratic(1,0,1), [])        
        # x + 2 = 0 has one solutions
        self.assertEqual(solveIntegerQuadratic(0,1,2), [-2])
        # 2x + 1 = 0 has no solutions
        self.assertEqual(solveIntegerQuadratic(0,2,1), [])
        for e in range(-10,10):
            for f in range(-10,10):
                for a in range(-10,10):
                    for b in range(-10,10):
                        if a*b*e*f != 0:
                            solns = solveIntegerLinear(e,a) + solveIntegerLinear(f,b)
                            solns.sort()
                            self.assertEqual(solveIntegerQuadratic(e*f,f*a+e*b,a*b),solns)

        triangles = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120]
        for i in range(-10,121):
            if isTriangle(i):
                self.assertEqual( i in triangles, True)
            else:
                self.assertEqual( i in triangles, False)
                
if __name__ == '__main__':
    unittest.main()