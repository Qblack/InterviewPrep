__author__ = 'Q'


class HashTable:
    _LOAD_FACTOR = 5
    def __init__(self, initial_capacity):
        self._slots = initial_capacity
        self._table = [[]]*initial_capacity
        self._size = 0

    def insert(self, key, value):
        slot = self._find_slot(key)

        #Check if key is in there
        found = False
        index = 0
        while not found and index < len(slot):
            if slot[index][0] == key:
                found = True
            index += 1
        if not found:
            slot.append((key, value))
            if len(slot)>= self._LOAD_FACTOR:
                self._rehash()

        return

    def remove(self, key):
        slot = self._find_slot(key)
        found = False
        index = 0
        while not found and index < len(slot):
            if slot[index][0] == key:
                found = True
                slot.remove(index)
            index += 1

        return

    def is_empty(self):
        empty = True
        index = 0
        while empty and index <= len(self._table):
            if len(self._table[index]) != 0:
                empty = False
            index += 1
        return empty

    def find(self, key):
        slot = self._find_slot(key)
        found = False
        index = 0
        value = None
        while not found and index < len(slot):
            if slot[index][0] == key:
                found = True
                value = slot[index][1]

        return value

    def __len__(self):
        length = 0
        for bucket in self._table:
            length += len(bucket)
        return length

    def __contains__(self, key):
        found = False
        index = 0
        slot = self._find_slot(key)
        while not found and index < len(slot):
            if slot[index][0] == key:
                found = True
            index += 1
        return found

    def _rehash(self):
        old_table = self._table
        self._slots = self._slots * 2 + 1
        self._table = [[]]*self._slots
        for slot in old_table:
            for element in slot:
                self.insert(element[0], element[1])

        return

    def _find_slot(self, key):
        hashkey = hash(key) % self._slots
        slot = self._table[hashkey]
        return slot

    def print_(self):
        for slot in self._table:
            for value in slot:
                print(value)
        return





