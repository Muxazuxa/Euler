from largest_palindrom import palindrom
import unittest

class Test(unittest.TestCase):

    def test_is_int(self):
        self.assertEqual(palindrom(2.1), 'Number must be Integer!')

    def test_positive_number(self):
        self.assertEqual(palindrom(-1), 'Number must be greater 1')

    def test_answer(self):
        self.assertTrue(palindrom(3), 9009)


if __name__ == '__main__':
    unittest.main()