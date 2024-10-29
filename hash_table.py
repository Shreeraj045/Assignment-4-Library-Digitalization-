from prime_generator import get_next_size

class HashTable:
    def __init__(self, collision_type, params):
        if collision_type == "Chain":
            self.z, self.table_size = params
        elif collision_type == "Linear":
            self.z, self.table_size = params
        elif collision_type == "Double":
            self.z1, self.z2, self.c2, self.table_size = params

        self.collision_type = collision_type
        self.table = [None] * self.table_size
        self.count = 0

    def get_int_from_str(self, char):
        if ord(char) >= ord('a'):
            return ord(char) - ord('a')
        else:
            return ord(char) - ord('A') + 26

    def polynomial_accumulation_hash(self, key, z, m):
        h = 0
        for char in reversed(key):
            h = h * z + self.get_int_from_str(char)
        return h % m

    def get_slot(self, key):
        if self.collision_type == "Double":
            return self.polynomial_accumulation_hash(key, self.z1, self.table_size)
        else:
            return self.polynomial_accumulation_hash(key, self.z, self.table_size)

    def get_step(self, key):
        h2 = self.polynomial_accumulation_hash(key, self.z2, self.c2)
        return self.c2 - h2

    def chain_insert(self, key, value):
        slot = self.get_slot(key)
        bucket = self.table[slot]
        if bucket is None:
            self.table[slot] = [value]
            self.count += 1
            return True
        for item in bucket:
            if self.get_key(item) == key:
                return False
        bucket.append(value)
        self.count += 1
        return True

    def _probe_insert(self, key, value, get_next_slot):
        if self.get_load() >= 1:
            return False
        slot = self.get_slot(key)
        for i in range(self.table_size):
            current_slot = get_next_slot(slot, i)
            if self.table[current_slot] is None:
                self.table[current_slot] = value
                self.count += 1
                return True
            if self.get_key(self.table[current_slot]) == key:
                return True
        return False

    def linear_insert(self, key, value):
        return self._probe_insert(key, value,lambda slot, i: (slot + i) % self.table_size)

    def double_insert(self, key, value):
        step = self.get_step(key)
        return self._probe_insert(key, value, lambda slot, i: (slot + i * step) % self.table_size)

    def insert(self, x):
        success = False
        if self.collision_type == "Chain":
            success = self.chain_insert(self.get_key(x), x)
        elif self.collision_type == "Linear":
            success = self.linear_insert(self.get_key(x), x)
        elif self.collision_type == "Double":
            success = self.double_insert(self.get_key(x), x)
        return success

    def find(self, key):
        slot = self.get_slot(key)
        bucket = self.table[slot]
        if self.collision_type == "Chain":
            bucket = self.table[slot]
            if bucket is not None:
                for item in bucket:
                    if self.get_key(item) == key:
                        return item
            return None

        elif self.collision_type == "Linear":
            for i in range(self.table_size):
                current_slot = (slot + i) % self.table_size
                if self.table[current_slot] is None:
                    return None
                if self.get_key(self.table[current_slot]) == key:
                    return self.table[current_slot]

        elif self.collision_type == "Double":
            step = self.get_step(key)
            for i in range(self.table_size):
                current_slot = (slot + i * step) % self.table_size
                if self.table[current_slot] is None:
                    return None
                if self.get_key(self.table[current_slot]) == key:
                    return self.table[current_slot]
        return None

    def get_load(self):
        return self.count / self.table_size

    def get_key(self, x):
        raise NotImplementedError("Subclass must implement get_key method")

    def format_item(self, x):
        raise NotImplementedError("Subclass must implement format_item method")

    def __str__(self):
        result = []
        if self.collision_type == "Chain":
            for slot in self.table:
                if slot is None:
                    result.append("<EMPTY>")
                elif not slot:
                    result.append("")
                else:
                    result.append(" ; ".join(self.format_item(item) for item in slot))
        else:
            for slot in self.table:
                if slot is None:
                    result.append("<EMPTY>")
                else:
                    result.append(self.format_item(slot))
        return " | ".join(result)
    def rehash(self):
        old_table = self.table
        self.table_size = get_next_size()
        self.table = [None] * self.table_size
        self.count = 0

        if self.collision_type == "Chain":
            for bucket in old_table:
                if bucket:
                    for item in bucket:
                        self.insert(item)
        else:
            for item in old_table:
                if item is not None:
                    self.insert(item)


class HashSet(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)

    def get_key(self, x):
        return x

    def format_item(self, item):
        return str(item)

    def find(self, key):
        result = super().find(key)
        return result is not None


class HashMap(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)

    def get_key(self, x):
        return x[0]

    def format_item(self, item):
        if item is None:
            return ""
        key, value = item
        return f"({key}, {value})"

    def find(self, key):
        result = super().find(key)
        return result[1] if result is not None else None