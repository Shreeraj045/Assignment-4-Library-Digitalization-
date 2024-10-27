from prime_generator import get_next_size

class HashTable:
    def __init__(self, collision_type, params):
        if collision_type == "Chain":
            self.z, self.size = params
        elif collision_type == "Linear":
            self.z, self.size = params
        elif collision_type == "Double":
            self.z1, self.z2, self.c2, self.size = params

        self.collision_type = collision_type
        self.table = [None] * self.size
        self.count = 0

    def get_int_from_str(self, char):
        if ord(char) >= ord('a'):
            return ord(char) - ord('a')
        else:
            return ord(char) - ord('A') + 26

    def polynomial_accumulation_hash(self, key, z, m):  # Added m parameter
        h = 0
        for char in reversed(key):  # reversed is correct!
            h = h * z + self.get_int_from_str(char)
        return h % m

    def get_slot(self, key):
        if self.collision_type == "Double":
            return self.polynomial_accumulation_hash(key, self.z1, self.size)
        else:
            return self.polynomial_accumulation_hash(key, self.z, self.size)

    def get_step(self, key):
        # Calculate h2 with modulo c2 instead of size
        h2 = self.polynomial_accumulation_hash(key, self.z2, self.c2)
        return self.c2 - h2  # Remove the extra modulo operation

    def chain_insert(self, key, value):
        slot = self.get_slot(key)
        if self.table[slot] is None:
            self.table[slot] = []
        for item in self.table[slot]:
            if self.get_key(item) == key:
                return False
        self.table[slot].append(value)
        return True

    def linear_insert(self, key, value):
        if self.get_load() >= 1:
            return False

        slot = self.get_slot(key)
        i = 0
        first_empty = -1

        while i < self.size:
            current_slot = (slot + i) % self.size

            if self.table[current_slot] is None:
                if first_empty == -1:
                    first_empty = current_slot
                break

            if self.get_key(self.table[current_slot]) == key:
                return False

            i += 1

        if first_empty != -1:
            self.table[first_empty] = value
            return True
        return False

    def double_insert(self, key, value):
        """
        Insert a key-value pair using double hashing.
        Returns True if insertion/update successful, False otherwise.
        """
        # Check if table is full
        if self.get_load() >= 1:
            return False

        # Get initial slot and step size
        initial_slot = self.get_slot(key)
        step_size = self.get_step(key)

        # Keep track of probing sequence
        current_slot = initial_slot
        probes = 0
        first_empty = -1

        # Probe until we find the key or have checked all slots
        while probes < self.size:
            # If slot is empty
            if self.table[current_slot] is None:
                # Remember first empty slot
                if first_empty == -1:
                    first_empty = current_slot
                # We can stop probing since all subsequent slots must be empty
                break

            # If we find the key, update the value
            elif self.get_key(self.table[current_slot]) == key:
                self.table[current_slot] = value
                return True

            # Move to next probe position
            probes += 1
            current_slot = (initial_slot + probes * step_size) % self.size

        # If we found an empty slot and key doesn't exist
        if first_empty != -1:
            self.table[first_empty] = value
            return True

        return False

    def insert(self, x):
        success = False
        if self.collision_type == "Chain":
            success = self.chain_insert(self.get_key(x), x)
        elif self.collision_type == "Linear":
            success = self.linear_insert(self.get_key(x), x)
        elif self.collision_type == "Double":
            success = self.double_insert(self.get_key(x), x)

        if success:
            self.count += 1

    def find(self, key):
        slot = self.get_slot(key)

        if self.collision_type == "Chain":
            if self.table[slot] is None:
                return None
            for item in self.table[slot]:
                if self.get_key(item) == key:
                    return item
            return None

        elif self.collision_type == "Linear":
            i = 0
            while i < self.size:
                current_slot = (slot + i) % self.size
                if self.table[current_slot] is None:
                    return None
                if self.get_key(self.table[current_slot]) == key:
                    return self.table[current_slot]
                i += 1
            return None

        elif self.collision_type == "Double":
            step = self.get_step(key)
            i = 0
            while i < self.size:
                current_slot = (slot + i * step) % self.size
                if self.table[current_slot] is None:
                    return None
                if self.get_key(self.table[current_slot]) == key:
                    return self.table[current_slot]
                i += 1
            return None

    def get_load(self):
        return self.count / self.size

    def get_key(self, x):
        raise NotImplementedError("Subclass must implement get_key method")

    def format_item(self, x):
        raise NotImplementedError("Subclass must implement format_item method")

    def __str__(self):
        result = []
        for slot in self.table:
            if slot is None:
                result.append("<EMPTY>")
            elif self.collision_type == "Chain" and isinstance(slot, list):
                if not slot:
                    result.append("")
                else:
                    result.append(" ; ".join(self.format_item(item) for item in slot))
            else:
                result.append(self.format_item(slot))
        return " | ".join(result)

    def rehash(self):
        old_table = self.table
        self.size = get_next_size()
        self.table = [None] * self.size
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