from math import sqrt

class BasicPrimes:
    def isPrime(self, n):
        if n < 2:
            return False
        if n % 2 == 0:
            return n == 2

        sqr = int(sqrt(n)) + 1

        for number in range(2, sqr):
            if n % number == 0:
                return False
        
        return True
