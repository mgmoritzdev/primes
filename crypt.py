class Crypt:
    def __init__(self, primesAlgorithm):
        self.primes = primesAlgorithm

    def isPrime(self, n):
        return self.primes.isPrime(n);

    def previousPrime(self, n):
        while (n > 1):
            n -= 1
            if self.primes.isPrime(n):
                return n

    def nextPrime(self, n):
        while (True):
            n += 1
            if self.primes.isPrime(n):
                return n

            
    def nthPrimeAfterNumber(self, skip, start):
        number = start
        for i in range(skip):
            number = self.nextPrime(number)
        return number
