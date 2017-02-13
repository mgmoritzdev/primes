import sys
import random

class MillerRabinPrimes:
    def isPrime(self, n):

        #https://inventwithpython.com/rabinMiller.py
        
        lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]        
        
        if n < 2:
            return False
        
        if n in lowPrimes:
            return True

        for prime in lowPrimes:
            if (n % prime == 0):
                return False

        # n - 1 = (s * 2^t)
        s = n - 1
        t = 0
        while s % 2 == 0:
            # keep halving s while it is even (and use t
            # to count how many times we halve s)
            s = s // 2
            t += 1

        for trials in range(5): # try to falsify n's primality 5 times
            a = random.randrange(2, n - 1)
            v = pow(a, s, n)
            if v != 1: # this test does not apply if v is 1.
                i = 0
                while v != (n - 1):
                    if i == t - 1:
                        return False
                    else:
                        i = i + 1
                        v = (v ** 2) % n
        return True

    #https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Primality_Testing
    def wikiBooksisPrime(self, n):
        """Use Rabin-Miller algorithm to return True (n is probably prime)
        or False (n is definitely composite)"""

        k = 7
   
        if n < 6:  # assuming n >= 0 in all cases... shortcut small cases here
            return [False, False, True, True, False, True][n]
        elif n & 1 == 0:  # should be faster than n % 2
            return False
        else:
            s, d = 0, n - 1
            while d & 1 == 0:
                s, d = 0, n - 1
            # Use random.randint(2, n-2) for very large numbers
            for a in random.sample(xrange(2, min(n - 2, sys.maxint)), min(n - 4, k)):
                x = pow(a, d, n)
                if x != 1 and x + 1 != n:
                    for r in xrange(1, s):
                        x = pow(x, 2, n)
                        if x == 1:
                            return False  # composite for sure
                        elif x == n - 1:
                            a = 0  # so we know loop didn't continue to end
                            break  # could be strong liar, try another a
                    if a:
                        return False  # composite if we reached end of this loop
            return True  # probably prime if reached end of outer loop
