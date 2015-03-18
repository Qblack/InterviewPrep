__author__ = 'Q'

import unittest
from Sorts import sorts


class SortTests(unittest.TestCase):
    TESTS = [
            ([], []),
            ([1], [1]),
            ([2, 1], [1, 2]),
            ([3, 2, 1], [1, 2, 3]),
            ([5, 9, 1, 6], [1, 5, 6, 9]),
            ([68, 89, 45, 10, 20], [10, 20, 45, 68, 89])]

    def test_bubble_sort(self):
        for test in SortTests.TESTS:
            sorts.bubble_sort(test[0])
            self.assertEqual(test[0], test[1])


if __name__ == '__main__':
    unittest.main()
