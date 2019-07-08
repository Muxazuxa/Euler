from smallest_multiple import sm_mul
import unittest

class Test(unittest.TestCase):

    def test_answer(self):
        self.assertEqual(sm_mul(), 232792560)


if __name__ == '__main__':
    unittest.main()