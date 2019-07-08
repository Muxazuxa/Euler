from multiple_3_5 import multiple_3_5
import unittest

class Test(unittest.TestCase):

    def test_is_int(self):
        self.assertEqual(multiple_3_5(4.1), 'Number must be Integer!')

    def test_number_gt_3(self):
        self.assertEqual(multiple_3_5(3), 'Number must be greater 3')

    def test_answer(self):
        self.assertEqual(multiple_3_5(10), 23)


if __name__ == '__main__':
    unittest.main()