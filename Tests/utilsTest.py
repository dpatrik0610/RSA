import unittest
from utils import *

class RSATests(unittest.TestCase):
    def test_extended_euclidean(self):
        expected_x, expected_y = -2, 7
        result_x, result_y = extended_euclidean(93, 27)
        self.assertEqual(expected_x, result_x)
        self.assertEqual(expected_y, result_y)

        expected_x, expected_y = -2, 6863
        result_x, result_y = extended_euclidean(161280, 47)
        self.assertEqual(expected_x, result_x)
        self.assertEqual(expected_y, result_y)

        expected_x, expected_y = 7, -58
        result_x, result_y = extended_euclidean(141,17)
        self.assertEqual(expected_x, result_x)
        self.assertEqual(expected_y, result_y)

    def test_quick_pow(self):
        expected = 348
        result = quick_pow(2, 174, 349)
        self.assertEqual(expected, result)

        expected = 338
        result = quick_pow(2, 203, 407)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()