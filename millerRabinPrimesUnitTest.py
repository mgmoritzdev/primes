import unittest
import crypt
import millerRabinPrimes as mrPrimes

class MillerRabinPrimesBaseTestCase(unittest.TestCase):
  def setUp(self):
    self.longMessage = True
    self.crypt = crypt.Crypt(mrPrimes.MillerRabinPrimes())

class SmallerThanTwoIsPrimeTestCase(MillerRabinPrimesBaseTestCase):
  def runTest(self):
    self.assertEqual(self.crypt.isPrime(1), False, 'Wrong answer')

class TwoIsPrimeTestCase(MillerRabinPrimesBaseTestCase):
  def runTest(self):
    self.assertEqual(self.crypt.isPrime(2), True, 'Wrong answer')
    
class EvenLargerThanTwoIsPrimeTestCase(MillerRabinPrimesBaseTestCase):
  def runTest(self):
    self.assertEqual(self.crypt.isPrime(10), False, 'Wrong answer')

class SmallPrimeIsPrimeTestCase(MillerRabinPrimesBaseTestCase):
  def runTest(self):
    self.assertEqual(self.crypt.isPrime(3), True, 'Wrong answer')

class LittleBiggerPrimeIsPrimeTestCase(MillerRabinPrimesBaseTestCase):
  def runTest(self):
    self.assertEqual(self.crypt.isPrime(31), True, 'Wrong answer')

class EightDigitPrimeIsPrimeTestCase(MillerRabinPrimesBaseTestCase):
  def runTest(self):
    self.assertEqual(self.crypt.isPrime(10887407), True, 'Wrong answer')

class SmallNonPrimeIsPrimeTestCase(MillerRabinPrimesBaseTestCase):
  def runTest(self):
    self.assertEqual(self.crypt.isPrime(9), False, 'Wrong answer')

class LittleBiggerNonPrimeIsPrimeTestCase(MillerRabinPrimesBaseTestCase):
  def runTest(self):
    self.assertEqual(self.crypt.isPrime(39), False, 'Wrong answer')

class NextPrimeTestCase(MillerRabinPrimesBaseTestCase):
  def runTest(self):
    self.assertEqual(self.crypt.nextPrime(-31), 2, 'Wrong answer')
    self.assertEqual(self.crypt.nextPrime(-1), 2, 'Wrong answer')
    self.assertEqual(self.crypt.nextPrime(0), 2, 'Wrong answer')
    self.assertEqual(self.crypt.nextPrime(1), 2, 'Wrong answer')
    self.assertEqual(self.crypt.nextPrime(2), 3, 'Wrong answer')
    self.assertEqual(self.crypt.nextPrime(3), 5, 'Wrong answer')
    self.assertEqual(self.crypt.nextPrime(5), 7, 'Wrong answer')
    self.assertEqual(self.crypt.nextPrime(6), 7, 'Wrong answer')
    self.assertEqual(self.crypt.nextPrime(7), 11, 'Wrong answer')
    self.assertEqual(self.crypt.nextPrime(11), 13, 'Wrong answer')
    self.assertEqual(self.crypt.nextPrime(29), 31, 'Wrong answer')

class NthPrimeAfterNumberTestCase(MillerRabinPrimesBaseTestCase):
  def runTest(self):
    self.assertEqual(self.crypt.nthPrimeAfterNumber(3, 31), 43, 'the third prime after three primes in the list: 31, 37, 41, 43')
    
if __name__ == '__main__':
    unittest.main()
