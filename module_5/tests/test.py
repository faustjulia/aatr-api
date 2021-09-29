import unittest
from fractions import Fraction
from typing import List

from module_5.tdd import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        data: List = [1, 2, 3]
        result: int = sum(data)

        self.assertEqual(result, 6)

    def test_list_fraction(self):
        data: List = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result: Fraction = sum(data)

        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
