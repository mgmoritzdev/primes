import unittest
import crypt
import basicPrimes

class BasicPrimesBaseTestCase(unittest.TestCase):
  def setUp(self):
    self.longMessage = True
    self.crypt = crypt.Crypt(basicPrimes.BasicPrimes())

class SmallerThanTwoIsPrimeTestCase(BasicPrimesBaseTestCase):
  def runTest(self):
    self.assertEqual(self.crypt.isPrime(1), False, 'Wrong answer')

class TwoIsPrimeTestCase(BasicPrimesBaseTestCase):
  def runTest(self):
    self.assertEqual(self.crypt.isPrime(2), True, 'Wrong answer')
    
class EvenLargerThanTwoIsPrimeTestCase(BasicPrimesBaseTestCase):
  def runTest(self):
    self.assertEqual(self.crypt.isPrime(10), False, 'Wrong answer')

class SmallPrimeIsPrimeTestCase(BasicPrimesBaseTestCase):
  def runTest(self):
    self.assertEqual(self.crypt.isPrime(3), True, 'Wrong answer')

class LittleBiggerPrimeIsPrimeTestCase(BasicPrimesBaseTestCase):
  def runTest(self):
    self.assertEqual(self.crypt.isPrime(31), True, 'Wrong answer')

class EightDigitPrimeIsPrimeTestCase(BasicPrimesBaseTestCase):
  def runTest(self):
    self.assertEqual(self.crypt.isPrime(10887407), True, 'Wrong answer')

class SmallNonPrimeIsPrimeTestCase(BasicPrimesBaseTestCase):
  def runTest(self):
    self.assertEqual(self.crypt.isPrime(9), False, 'Wrong answer')

class LittleBiggerNonPrimeIsPrimeTestCase(BasicPrimesBaseTestCase):
  def runTest(self):
    self.assertEqual(self.crypt.isPrime(39), False, 'Wrong answer')

class NextPrimeTestCase(BasicPrimesBaseTestCase):
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

class NthPrimeAfterNumberTestCase(BasicPrimesBaseTestCase):
  def runTest(self):
    self.assertEqual(self.crypt.nthPrimeAfterNumber(3, 31), 43, 'the third prime after three primes in the list: 31, 37, 41, 43')
    
if __name__ == '__main__':
    unittest.main()
