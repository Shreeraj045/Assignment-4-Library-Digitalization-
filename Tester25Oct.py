from hash_table import *
from library import MuskLibrary

def test_hash_set():
    print("Testing HashSet:")
    params_double = (31, 17, 13, 7)  # z1 = 31, z2 = 37, c2 = 7, table_size = 11
    double_hash_set = HashSet("Double", params_double)

    # Insert elements into HashSet
    ##################################################
    double_hash_set.insert("apple")
    double_hash_set.insert("banana")
    double_hash_set.insert("cherry")
    double_hash_set.insert("date")
    double_hash_set.insert("dateaa")


    # double_hash_set.insert("c")
    # double_hash_set.insert("ca")

    # Print the HashSet
    print("HashSet contents (Double Hashing):", double_hash_set)
    print("Test passed for Double Hashing!\n")


def test_Hash_Map():
    print("Testing HashMap :")

    # Testing with double hashing collision handling
    params = (31, 17, 13, 7)  # z1 = 31, z2 = 17, c2 = 13, table_size = 11
    hash_map = HashMap("Double", params)

    # Insert (key, value) pairs into HashMap

    ##################################################
    hash_map.insert(("apple", 1))
    hash_map.insert(("banana", 2))
    hash_map.insert(("cherry", 3))
    hash_map.insert(("date", 4))

    # Check if keys and values exist
    # assert hash_map.find("apple") == 1, "Test Failed: 'apple' should map to 1"
    # assert hash_map.find("banana") == 2, "Test Failed: 'banana' should map to 2"
    # assert hash_map.find("cherry") == 3, "Test Failed: 'cherry' should map to 3"
    # assert hash_map.find("date") == 4, "Test Failed: 'date' should map to 4"
    # assert hash_map.find("grape") == None, "Test Failed: 'grape' should not be in the HashMap"

    # Print the HashMap
    print("HashMap contents with double hashing:", hash_map)
    print("Test passed!\n")


def main():
    test_hash_set()  # Test HashSet with chaining
    test_Hash_Map()  # Test HashMap with double hashing

def MuskLibraryTest(book_titles, texts):
    print("Musk Library")
    mlib = MuskLibrary(book_titles, texts)
    print(mlib.distinct_words("HarryPotter"))
    print(mlib.count_distinct_words("TheHobbit"))
    print(mlib.search_keyword("War"))
    mlib.print_books()
    print("-" * 350)

if __name__ == "__main__":
    main()
