import matplotlib.pyplot as plt
import numpy as np
from math import floor, ceil

from crypt import Crypt as C
from millerRabinPrimes import MillerRabinPrimes as MRP

# The ideia is to draw the graphics x,y of primes that may
# compose a composite (like an RSA number). The task is to
# watch the distance of y from a integer for a given x prime.

isPrime = C(MRP()).isPrime

class PrimesByErrors:
    def __init__(self, rsa):
        self.rsa = rsa

    def calculateErrors(self):
        sqr = int(pow(self.rsa, 0.5)) + 1
        self.primes = filter(isPrime, range(2, sqr))
        self.errors = map(self.getError, self.primes)

    def getError(self, n):
        cofactor = float(self.rsa) / n
        if cofactor == int(cofactor):
            return 0
        
        floorInteger = floor(cofactor)
        ceilInteger = ceil(cofactor)
        previousPrime = C(MRP()).previousPrime(int(cofactor))
        nextPrime = C(MRP()).nextPrime(int(cofactor))

        # print str(cofactor)
        # print str(previousPrime)
        # print str(nextPrime)

        #return cofactor
        #return min(cofactor - previousPrime, nextPrime - cofactor)
        #return cofactor-previousPrime
        #return nextPrime - cofactor
        return min(cofactor - floorInteger, ceilInteger - cofactor)

    def plotErrors(self):
        plt.plot(self.primes, self.errors, 'ro')
        plt.axis([2, max(self.primes), 0, max(self.errors)])        
        plt.show()

# import functionError as fe
# reload(fe)
# func =  fe.PrimesByErrors(11239*15877)
# func.calculateErrors()
