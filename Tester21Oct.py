def simulate_hash_insertion(text, z1=40, z2=35, c2=17, size=37):
    # Helper function to convert character to number (a-z: 0-25, A-Z: 26-51)
    def get_int_from_str(char):
        if ord(char) >= ord('a'):
            return ord(char) - ord('a')
        else:
            return ord(char) - ord('A') + 26

    # Polynomial accumulation hash function
    def polynomial_hash(key, z, m):
        h = 0
        for char in reversed(key):
            h = h * z + get_int_from_str(char)
        return h % m

    # Function to get step size for double hashing
    def get_step(key):
        h2 = polynomial_hash(key, z2, c2)
        return c2 - h2

    # Initialize empty hash table
    table = [None] * size
    current_state = []

    words = text.split()
    for word in words:
        # Calculate initial slot
        initial_slot = polynomial_hash(word, z1, size)
        step = get_step(word)

        # Find available slot
        current_slot = initial_slot
        probes = 0
        first_empty = -1

        while probes < size:
            if table[current_slot] is None:
                if first_empty == -1:
                    first_empty = current_slot
                break
            probes += 1
            current_slot = (initial_slot + probes * step) % size

        if first_empty != -1:
            table[first_empty] = word
            current_state = table.copy()
            print(f"\nInserting '{word}':")
            print(f"Initial hash (h1): {initial_slot}")
            print(f"Step size (h2): {step}")
            print(f"Placed at position: {first_empty}")
            print("Current table:", " | ".join(str(x) if x else "<EMPTY>" for x in current_state))


text = "To Kill a Mockingbird addresses injustice and race through the eyes of young Scout Finch"
simulate_hash_insertion(text)