__author__ = 'Q'


class HashTable:
    def __init__(self, initial_capacity, load_factor):
        self.load_factor = load_factor
        self.table = [[None] * initial_capacity]

    def insert(self, value):
        return False

    def remove(self, key):
        return False

    def is_empty(self):
        return False

    def find(self, key):
        return False

    def __len__(self):
        return False

    def __contains__(self, key):
        return True

    def _rehash(self):
        return False

    def _find_slot(self, key):
        return False





