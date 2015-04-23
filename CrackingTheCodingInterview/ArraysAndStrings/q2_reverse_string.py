__author__ = 'blac2410'


def reverse(s):
    front = 0

    mid = len(s) // 2
    n = len(s)
    back = n - 1

    while front < mid:
        s = ''.join((s[0:front], s[back], s[front + 1:back], s[front], s[back + 1:n]))
        front += 1
        back -= 1

    return s


import unittest


class TestReverse(unittest.TestCase):
    def test_single_character(self):
        s = 'a'
        expected = 'a'
        actual = reverse(s)
        self.assertEqual(expected, actual)

    def test_two_character(self):
        s = 'ab'
        expected = 'ba'
        actual = reverse(s)
        self.assertEqual(expected, actual)

    def test_three_character(self):
        s = 'abc'
        expected = 'cba'
        actual = reverse(s)
        self.assertEqual(expected, actual)

    def test_seven_character(self):
        s = 'abcdefg'
        expected = 'gfedcba'
        actual = reverse(s)
        self.assertEqual(expected, actual)

    def test_eight_character(self):
        s = 'abcdefgh'
        expected = 'hgfedcba'
        actual = reverse(s)
        self.assertEqual(expected, actual)