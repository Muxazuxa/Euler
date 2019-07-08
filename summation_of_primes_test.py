from summation_of_primes import summ_primes
import unittest

class Test(unittest.TestCase):

    def test_is_int(self):
        self.assertEqual(summ_primes(3.1), 'Number must be Integer!')

    def test_positive_number(self):
        self.assertEqual(summ_primes(-1), 'Number must be greater 2')

    def test_answer(self):
        self.assertTrue(summ_primes(10), 17)


if __name__ == '__main__':
    unittest.main()