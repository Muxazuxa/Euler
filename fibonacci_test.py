from fibonacci import fibonacci_even_sum
import unittest

class Test(unittest.TestCase):

    def test_is_int(self):
        self.assertEqual(fibonacci_even_sum(1.1), 'Number must be Integer!')

    def test_positive_number(self):
        self.assertEqual(fibonacci_even_sum(-1), 'Number must be positive')

    def test_answer(self):
        self.assertTrue(fibonacci_even_sum(10), 2+8) #2,8 First even numbers of Fibonacci lt 10


if __name__ == '__main__':
    unittest.main()