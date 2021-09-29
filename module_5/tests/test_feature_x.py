import unittest
from typing import List, Tuple

from module_5.tdd import sum


class TestSum(unittest.TestCase):

    def test_sum_whole_numbers(self):
        data: List = [1, 2, 3]
        result: int = sum(data)
        self.assertEqual(result, 6)

    def test_sum_from_tuple(self):
        data: Tuple = (1, 2, 3)
        result: int = sum(data)
        self.assertEqual(result, 6)

    def test_sum_negative_number(self):
        data: List = [-1, -2, -3]
        result: int = sum(data)
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
