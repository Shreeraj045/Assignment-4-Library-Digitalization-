from prime_generator import get_next_size

class HashTable:
    def __init__(self, collision_type, params):
        '''
        Possible collision_type:
            "Chain"     : Use hashing with chaining
            "Linear"    : Use hashing with linear probing
            "Double"    : Use double hashing
        '''
        if collision_type == "chaining":
            self.z, self.size = params
        elif collision_type == "linear":
            self.z, self.size = params
        elif collision_type == "double":
            self.z1, self.z2, self.c2, self.size = params

        self.collision_type = collision_type
        self.table = [None] * self.size
        self.count = 0  # Number of elements in the table
    def get_int_from_str(self,char):
        if ord(char) >= ord('a'):
            return ord(char)-ord('a')
        else:
            return ord(char) - ord('A') + 26
    def polynomial_accumulation_hash(self, key, z):
        ''' Optimized polynomial accumulation hash function with parameter z using Horner's method. '''
        h = 0
        for char in reversed(key):  # Traverse the string from the last character to the first.
            h = h * z + self.get_int_from_str(char)
        return h % self.size

    def get_slot(self, key):
        if self.collision_type == "double":
            return self.polynomial_accumulation_hash(key, self.z1)
        else:
            return self.polynomial_accumulation_hash(key, self.z)

    def get_step(self, key):
        ''' Secondary hash function for double hashing. '''
        h2 = self.polynomial_accumulation_hash(key, self.z2)
        return self.c2 - (h2 % self.c2)

    def chain_insert(self, key, value):
        ''' Handles collision using chaining (linked list of entries). '''
        slot = self.get_slot(key)
        if self.table[slot] is None:
            self.table[slot] = []  # Initialize a list if empty
        if value not in self.table[slot]:
            self.table[slot].append(value)
        # print(self.table)

    def linear_insert(self, key, value):
        ''' Handles collision using linear probing. '''
        slot = self.get_slot(key)
        i = 0
        if self.get_load() == 1:
            print("ERROR - List Full Already")
            return
        while self.table[(slot + i) % self.size] is not None :
            if self.table[(slot + i) % self.size] == value:
                return
            i += 1
        self.table[(slot + i) % self.size] = value
        # print(self.table)


    def double_insert(self, key, value):
        ''' Handles collision using double hashing. '''
        slot = self.get_slot(key)
        step = self.get_step(key)
        i = 0
        while self.table[(slot + i * step) % self.size] is not None:
            i += 1
            if value == self.table[(slot + i * step) % self.size]:
                return
        self.table[(slot + i * step) % self.size] = value

    def insert(self, x):
        key = x[0] if isinstance(x, tuple) else x
        if self.collision_type == "chaining":
            self.chain_insert(key, x)
        elif self.collision_type == "linear":
            self.linear_insert(key, x)
        elif self.collision_type == "double":
            self.double_insert(key, x)
        self.count += 1
        if self.get_load() > 0.75:
            self.rehash()

    def find(self, key):
        ''' Find the key in the hash table and return the corresponding value or True/False. '''
        slot = self.get_slot(key)
        if self.collision_type == "chaining":
            # Chaining: Traverse the linked list at the slot to find the key
            if self.table[slot] is None:
                return False
            for item in self.table[slot]:
                if isinstance(item, tuple):  # If items are stored as tuples
                    if item[0] == key:
                        return item
                else:
                    if item == key:  # For HashSet where items are stored directly
                        return item
            return False
        else:
            i = 0
            step = self.get_step(key) if self.collision_type == "double" else 1

            while True:
                current_slot = (slot + i * step) % self.size

                if self.table[current_slot] is None:
                    return False  # Key is not found, end of search

                if isinstance(self.table[current_slot], tuple):
                    if self.table[current_slot][0] == key:
                        return self.table[current_slot]  # Found key-value pair in HashMap

                elif self.table[current_slot] == key:
                    return self.table[current_slot]  # Found key in HashSet

                i += 1

                # To avoid infinite loops in probing
                if i > self.size:
                    return False  # Key not found, probing limit reached


    def get_load(self):
            return self.count / self.size

    def __str__(self):
        ''' Returns the string representation of the table in the specified format. '''
        result = []
        for slot in self.table:
            if slot is None:
                result.append("⟨EMPTY⟩")
            elif self.collision_type == "chaining" and isinstance(slot, list):
                if not slot:
                    result.append("")
                else:
                    result.append(" ; ".join(self.format_item(item) for item in slot))
            else:
                result.append(self.format_item(slot))
        return " | ".join(result)


    # TO BE USED IN PART 2 (DYNAMIC HASH TABLE)
    def rehash(self):
        pass

# IMPLEMENT ALL FUNCTIONS FOR CLASSES BELOW
# IF YOU HAVE IMPLEMENTED A FUNCTION IN HashTable ITSELF,
# YOU WOULD NOT NEED TO WRITE IT TWICE

class HashSet(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)

    def format_item(self, item):
        return str(item)

    def insert(self, key):
        # if self.find(key):  # Check if key already exists
            # print(1)
            # return None  # Do not add duplicate keys
        super().insert(key)

    def find(self, key):
        return super().find(key) is not None

    def get_slot(self, key):
        return super().get_slot(key)

    def get_load(self):
        return super().get_load()

    def __str__(self):
        return super().__str__()

class HashMap(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)

    def insert(self, x):
        key = x[0]
        if self.find(key):  # Check if key already exists
            print(1)
            return  # Do not add duplicate keys
        super().insert(x)

    def find(self, key):
        result = super().find(key)
        if result:
            return result[1]  # Return the value associated with the key
        return None

    def get_slot(self, key):
        return super().get_slot(key)

    def format_item(self, item):
        if item is None:
            return ""
        key, value = item
        return f"({key}, {value})"

    def get_load(self):
        return super().get_load()

    def __str__(self):
        return super().__str__()