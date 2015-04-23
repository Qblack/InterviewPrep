__author__ = 'blac2410'


def all_unique(s):
    is_unique = True
    if len(s) > 128:
        is_unique = False
    freq_array = [0] * 128
    i = 0
    while is_unique and i < len(s):
        char = s[i]
        index = ord(char)
        if freq_array[index] != 0:
            is_unique = False
        else:
            freq_array[index] += 1
        i += 1

    return is_unique


import unittest


class TestUnique(unittest.TestCase):
    def test_single_char_returns_true(self):
        expected = True
        s = 'a'
        actual = all_unique(s)
        self.assertEqual(expected, actual)

    def test_nonunique_returns_false(self):
        expected = False
        s = 'aa'
        actual = all_unique(s)
        self.assertEqual(expected, actual)

    def test_length_greater_than_128_returns_false(self):
        expected = False
        s = '1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+=-~`{}[]:";<>?/.,aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        actual = all_unique(s)
        self.assertEqual(expected, actual)

    def test_allcharacters_i_can_think_of_returns_true(self):
        expected = True
        s = '1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+=-~`{}[]:";<>?/.,'
        actual = all_unique(s)
        self.assertEqual(expected, actual)