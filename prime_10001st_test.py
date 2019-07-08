from prime_10001st import eratoshpene
import unittest

class Test(unittest.TestCase):

    def test_is_int(self):
        self.assertEqual(eratoshpene(1.1), 'Number must be Integer!')

    def test_positive_number(self):
        self.assertEqual(eratoshpene(-1), 'Number must be positive')

    def test_answer(self):
        self.assertTrue(eratoshpene(5), 13)


if __name__ == '__main__':
    unittest.main()