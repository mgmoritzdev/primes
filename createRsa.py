from random import random

from crypt import Crypt as C
from millerRabinPrimes import MillerRabinPrimes as MRP

mrp = C(MRP())

def getPrime(numberOfDigits):
    r = int(random() * 10**numberOfDigits)
    p = mrp.nextPrime(r)
    
    return p

def getRsaLikePair(numberOfDigits):
    return [getPrime(numberOfDigits), getPrime(numberOfDigits)]
