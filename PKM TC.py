from hash_table import HashSet, HashMap


def check_hash_set():
    print("Checking HashSet...")

    # Test Chaining
    print("Test Chaining:")
    hs_chaining = HashSet(collision_type="Chain", params=[31, 10])
    hs_chaining.insert("apple")
    hs_chaining.insert("banana")
    hs_chaining.insert("orange")
    assert hs_chaining.find("apple"), "Failed to find 'apple' in chaining HashSet"
    assert not hs_chaining.find("grape"), "'grape' shouldn't be found in chaining HashSet"
    print(hs_chaining)

    # Test Linear Probing
    print("\nTest Linear Probing:")
    hs_linear = HashSet(collision_type="Linear", params=[31, 10])
    hs_linear.insert("a")
    hs_linear.insert("cat")
    hs_linear.insert("dog")
    hs_linear.insert("bat")

    assert hs_linear.find("dog"), "Failed to find 'dog' in linear HashSet"
    assert not hs_linear.find("fish"), "'fish' shouldn't be found in linear HashSet"
    print(hs_linear)

    # Test Double Hashing
    print("\nTest Double Hashing:")
    hs_double = HashSet(collision_type="Double", params=[31, 37, 7, 10])
    hs_double.insert("red")
    hs_double.insert("blue")
    hs_double.insert("green")
    assert hs_double.find("blue"), "Failed to find 'blue' in double hashing HashSet"
    assert not hs_double.find("yellow"), "'yellow' shouldn't be found in double hashing HashSet"
    print(hs_double)

    print("HashSet tests passed.\n")


def check_hash_map():
    print("Checking HashMap...")

    # Test Chaining
    print("Test Chaining:")
    hm_chaining = HashMap(collision_type="Chain", params=[31, 10])
    hm_chaining.insert(("apple", 100))
    hm_chaining.insert(("banana", 200))
    hm_chaining.insert(("orange", 300))
    assert hm_chaining.find("apple") == 100, "Failed to find value for 'apple' in chaining HashMap"
    assert hm_chaining.find("grape") is None, "'grape' shouldn't be found in chaining HashMap"
    print(hm_chaining)

    # Test Linear Probing
    print("\nTest Linear Probing:")
    hm_linear = HashMap(collision_type="Linear", params=[31, 10])
    hm_linear.insert(("cat", 1))
    hm_linear.insert(("dog", 2))
    hm_linear.insert(("bat", 3))
    assert hm_linear.find("dog") == 2, "Failed to find value for 'dog' in linear HashMap"
    assert hm_linear.find("fish") is None, "'fish' shouldn't be found in linear HashMap"
    print(hm_linear)

    # Test Double Hashing
    print("\nTest Double Hashing:")
    hm_double = HashMap(collision_type="Double", params=[31, 37, 7, 10])
    hm_double.insert(("red", 50))
    hm_double.insert(("blue", 100))
    hm_double.insert(("green", 150))
    assert hm_double.find("blue") == 100, "Failed to find value for 'blue' in double hashing HashMap"
    assert hm_double.find("yellow") is None, "'yellow' shouldn't be found in double hashing HashMap"
    print(hm_double)

    print("HashMap tests passed.\n")


if __name__ == "__main__":
    check_hash_set()
    check_hash_map()
    print("All tests completed successfully.")