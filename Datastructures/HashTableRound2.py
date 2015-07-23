__author__ = 'Q'


class HashTable:
    LOAD_FACTOR = 5

    def __init__(self, size):
        self._size = size
        self._slots = []
        self._count = 0
        for _ in range(size):
            self._slots.append([])

    def __contains__(self,item):
        slot = self._find_slot(item.key)
        index = 0
        found = False
        while not found and index < len(slot):
            if slot[index].key == item.key:
                found = True
            else:
                index += 1
        return found

    def __len__(self):
        return self._count

    def _find_slot(self, key):
        slot_number = hash(key) % self._size
        return self._slots[slot_number]

    def _rehash(self):
        temp_slots = self._slots
        self._slots = []
        self._size = self._size * 2 + 1
        [self._slots.append([]) for _ in range(self._size)]
        for old_slot in temp_slots:
            for item in old_slot:
                slot = self._find_slot(item.key)
                slot.append(item)

        return

    def is_empty(self):
        return self._count==0

    def insert(self, item):
        slot = self._find_slot(item.key)
        if item in slot:
            return False
        else:
            slot.append(item)
            self._count += 1

        if self._count / self._size > HashTable.LOAD_FACTOR:
            self._rehash()
        return True

    def remove(self, key):
        slot = self._find_slot(key)
        index = 0
        found = False
        while not found and index < len(slot):
            if slot[index].key == key:
                found = True
                del slot[index]
            else:
                index += 1
        return found

    def find(self, key):
        slot = self._find_slot(key)
        index = 0
        found = False
        while not found and index < len(slot):
            if slot[index].key == key:
                found = True
            else:
                index += 1
        if found:
            return slot[index].vlaue

        return None

    def debug(self):
        for i, slot in enumerate(self._slots):
            print("SLOT: {0}".format(i))
            print("------------------------")
            for item in slot:
                print(item)



