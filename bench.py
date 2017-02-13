import timeit

from crypt import Crypt as C
from basicPrimes import BasicPrimes as BP
from millerRabinPrimes import MillerRabinPrimes as MRP

p1 = C(BP())
p2 = C(MRP())

t1 = timeit.Timer('p1.isPrime(10887407)', 'from __main__ import p1')
t2 = timeit.Timer('p2.isPrime(10887407)', 'from __main__ import p2')

numberOfTimesToRun = 10000

print "\nRunning primality test with seven digit number 10.000 times\n"
print "Time of basic primality test: " + str(t1.timeit(numberOfTimesToRun))
print "Time of miller-rabin primality test: " + str(t2.timeit(numberOfTimesToRun))


        
    
