from hash_table import HashSet, HashMap
from prime_generator import get_next_size

class DynamicHashSet(HashSet):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)

    def insert(self, key):
        super().insert(key)
        if self.get_load() >= 0.5:
            super().rehash()


class DynamicHashMap(HashMap):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
    def insert(self, key):
        super().insert(key)

        if self.get_load() >= 0.5:
            self.rehash()