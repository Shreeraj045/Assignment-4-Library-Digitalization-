from hash_table import *


def test_hash_set():
    print("Testing HashSet:")

    # Testing with chaining collision handling
    print("Testing Chaining:")
    params = (31, 11)  # z = 31, table_size = 11
    hash_set = HashSet("chaining", params)

    # Insert elements into HashSet
    hash_set.insert("a")
    hash_set.insert("a")
    hash_set.insert("a")
    hash_set.insert("a")
    hash_set.insert("a")
    hash_set.insert("a")
    hash_set.insert("aa")
    hash_set.insert("aaa")
    hash_set.insert("baa")
    hash_set.insert("faaaa")
    # Print the HashSet
    print("HashSet contents:", hash_set)
    print("Test passed!\n")

    print("Testing Linear Probing:")
    params_linear = (31, 11)  # z = 31, table_size = 11
    linear_hash_set = HashSet("linear", params_linear)

    # Insert elements into HashSet
    linear_hash_set.insert("a")
    linear_hash_set.insert("a")
    linear_hash_set.insert("a")
    linear_hash_set.insert("a")
    linear_hash_set.insert("e")
    linear_hash_set.insert("f")
    linear_hash_set.insert("aaa")
    linear_hash_set.insert("abc")
    linear_hash_set.insert("ee")
    linear_hash_set.insert("baa")
    linear_hash_set.insert("faaaa")
    # Print the HashSet
    print("HashSet contents (Linear Probing):", linear_hash_set)
    print("Test passed for Linear Probing!\n")

    print("Testing Double Hashing:")
    params_double = (31, 37, 7, 11)  # z1 = 31, z2 = 37, c2 = 7, table_size = 11
    double_hash_set = HashSet("double", params_double)

    # Insert elements into HashSet
    double_hash_set.insert("a")
    double_hash_set.insert("a")
    double_hash_set.insert("b")
    double_hash_set.insert("ba")
    double_hash_set.insert("c")
    double_hash_set.insert("ca")

    # Print the HashSet
    print("HashSet contents (Double Hashing):", double_hash_set)
    print("Test passed for Double Hashing!\n")


def test_hash_map():
    print("Testing HashMap:")

    # Testing with linear probing collision handling
    print("Testing Linear Probing:")
    params = (31, 11)  # z = 31, table_size = 11
    hash_map = HashMap("linear", params)

    # Insert (key, value) pairs into HashMap
    hash_map.insert(("apple", 1))
    hash_map.insert(("banana", 2))
    hash_map.insert(("cherry", 3))
    hash_map.insert(("date", 4))
    hash_map.insert(("datea",5))
    hash_map.insert(("dateaa",6))
    hash_map.insert(("dateaaa", 7))

    # Check if keys and values exist
    assert hash_map.find("apple") == 1, "Test Failed: 'apple' should map to 1"
    assert hash_map.find("banana") == 2, "Test Failed: 'banana' should map to 2"
    assert hash_map.find("grape") == None, "Test Failed: 'grape' should not be in the HashMap"

    # Print the HashMap
    print("HashMap contents:", hash_map)
    print("Test passed!\n")


def test_double_hashing():
    print("Testing HashMap with Double Hashing:")

    # Testing with double hashing collision handling
    params = (31, 17, 13, 11)  # z1 = 31, z2 = 17, c2 = 13, table_size = 11
    hash_map = HashMap("double", params)

    # Insert (key, value) pairs into HashMap
    hash_map.insert(("apple", 1))
    hash_map.insert(("banana", 2))
    hash_map.insert(("cherry", 3))
    hash_map.insert(("date", 4))

    # Check if keys and values exist
    assert hash_map.find("apple") == 1, "Test Failed: 'apple' should map to 1"
    assert hash_map.find("banana") == 2, "Test Failed: 'banana' should map to 2"
    assert hash_map.find("cherry") == 3, "Test Failed: 'cherry' should map to 3"
    assert hash_map.find("date") == 4, "Test Failed: 'date' should map to 4"
    assert hash_map.find("grape") == None, "Test Failed: 'grape' should not be in the HashMap"

    # Print the HashMap
    print("HashMap contents with double hashing:", hash_map)
    print("Test passed!\n")


def main():
    test_hash_set()  # Test HashSet with chaining
    test_hash_map()  # Test HashMap with linear probing
    test_double_hashing()  # Test HashMap with double hashing


if __name__ == "__main__":
    main()
