
__author__ = 'Q'

import unittest
from Datastructures.HashTableRound2 import HashTable

class KeyValuePair:
    def __init__(self,key,value):
        self.key = key
        self.value = value


SIZE = 7
class HashTableTests(unittest.TestCase):

    def setUp(self):
        self.hash_table = HashTable(SIZE)

    def test_len_emptyTable_returns0(self):
        self.assertEqual(0, len(self.hash_table))

    def test_len_tableWithOne_returns1(self):
        self.hash_table.insert(KeyValuePair('red','apples'))
        self.assertEqual(1, len(self.hash_table))

    def test_len_tableWithTwo_returns2(self):
        self.hash_table.insert(KeyValuePair('red','apples'))
        self.hash_table.insert(KeyValuePair('orange','orange'))
        self.assertEqual(2, len(self.hash_table))

    def test_isempty_empty_true(self):
        self.assertTrue(self.hash_table.is_empty())

    def test_isempty_empty_false(self):
        self.hash_table.insert(KeyValuePair('red','apples'))
        self.assertFalse(self.hash_table.is_empty())

    def test_insert_valueInsertedToCorrectRow(self):
        hashkey = hash('red') % SIZE
        self.hash_table.insert(KeyValuePair('red','apples'))
        slot = self.hash_table._slots[hashkey]
        slot[0] = (KeyValuePair('red','apples'))

    def test_remove(self):
        self.hash_table.insert(KeyValuePair('red','apples'))
        self.hash_table.remove('red')
        self.assertEqual(0, len(self.hash_table))

    def test_find_empty_returnsNone(self):
        value = self.hash_table.find('red')
        self.assertIsNone(value)

    def test_find_nonEmpty_returnsElement(self):
        self.hash_table.insert(KeyValuePair('red','apples'))
        value = self.hash_table.find('red')
        self.assertEqual('apples', value)

    def test_contains_False(self):
        self.assertFalse('red' in self.hash_table)

    def test_contains_True(self):
        self.hash_table.insert(KeyValuePair('red','apples'))
        self.assertTrue('red' in self.hash_table)

    def test_rehash_called(self):
        small_hash = HashTable(1)
        for i in range(0, small_hash.LOAD_FACTOR):
            small_hash.insert(KeyValuePair(i, i))

        small_hash.insert(KeyValuePair(6,6))
        self.assertEqual(3, len(small_hash._slots))
        self.assertEqual(6, len(small_hash))


if __name__ == '__main__':
    unittest.main()
