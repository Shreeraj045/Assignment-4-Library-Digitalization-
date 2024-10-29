import time
from prime_generator import set_primes, get_next_size
from hash_table import HashSet, HashMap
from dynamic_hash_table import DynamicHashSet, DynamicHashMap
from library import MuskLibrary, JGBLibrary


def progress_bar(iterable, prefix='', suffix='', decimals=1, length=50, fill='█', printEnd="\r"):
    total = len(iterable)

    def printProgressBar(iteration):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)

    printProgressBar(0)
    for i, item in enumerate(iterable):
        yield item
        printProgressBar(i + 1)
    print()


def test_hash_set():
    print("\nTesting HashSet Implementation...")
    tests = [
        ("Linear", (3, 37)),
        ("Double", (3, 5, 7, 37)),
        ("Chain", (3, 37))
    ]

    for collision_type, params in progress_bar(tests, prefix='Progress:', suffix='Complete', length=50):
        print(f"\nTesting {collision_type} Collision Resolution:")

        # Initialize HashSet
        hash_set = HashSet(collision_type, params)

        # Test basic insertion and find
        test_words = ["apple", "banana", "cherry", "date", "elderberry"]
        for word in test_words:
            hash_set.insert(word)
            if (hash_set.find(word) == False):
                print(collision_type, word)
            assert hash_set.find(word) == True, f"Failed to find {word} after insertion"

        # Test duplicate insertion
        for word in test_words:
            hash_set.insert(word)
            assert hash_set.get_load() == len(test_words) / params[-1], "Load factor changed after duplicate insertion"

        # Test non-existent elements
        assert hash_set.find("nonexistent") == False, "Found non-existent element"

        # Test slot retrieval
        for word in test_words:
            slot = hash_set.get_slot(word)
            assert slot is not None, f"Slot not found for existing word {word}"

        print(f"Load factor: {hash_set.get_load():.2f}")
        print(f"Final table: {hash_set}")


def test_hash_map():
    print("\nTesting HashMap Implementation...")
    tests = [
        ("Linear", (3, 37)),
        ("Double", (3, 5, 7, 37)),
        ("Chain", (3, 37))
    ]

    for collision_type, params in progress_bar(tests, prefix='Progress:', suffix='Complete', length=50):
        print(f"\nTesting {collision_type} Collision Resolution:")

        # Initialize HashMap
        hash_map = HashMap(collision_type, params)

        # Test key-value insertion and retrieval
        test_pairs = [
            ("booka", "The Hobbit"),
            ("bookb", "vivek"),
            ("bookc", "Dune"),
            ("bookd", "Foundation"),
            ("booke", "Neuromancer")
        ]

        for key, value in test_pairs:
            hash_map.insert((key, value))
            assert hash_map.find(key) == value, f"Wrong value retrieved for {key}"

        # Test duplicate key insertion (should keep original value)
        original_value = hash_map.find("booka")
        hash_map.insert(("booka", "The Lord of the Rings"))
        assert hash_map.find("booka") == original_value, "Original value was not preserved for duplicate key"
        assert hash_map.get_load() == len(test_pairs) / params[-1], "Load factor changed after duplicate insertion"

        # Test non-existent keys
        assert hash_map.find("nonexistent") is None, "Found value for non-existent key"

        # Test slot retrieval
        for key, _ in test_pairs:
            slot = hash_map.get_slot(key)
            assert slot is not None, f"Slot not found for existing key {key}"

        print(f"Load factor: {hash_map.get_load():.2f}")
        # print(f"Final table: {hash_map}")


def test_dynamic_hash_set():
    print("\nTesting DynamicHashSet Implementation...")
    # Set up prime numbers for rehashing
    set_primes([5, 7, 11, 13, 17, 19, 23, 29, 37])
    tests = [
        ("Linear", (3, 5)),
        ("Double", (3, 5, 7, 11)),
        ("Chain", (3, 5))
    ]

    for collision_type, params in progress_bar(tests, prefix='Progress:', suffix='Complete', length=50):
        print(f"\nTesting {collision_type} Collision Resolution:")

        dynamic_set = DynamicHashSet(collision_type, params)
        initial_size = dynamic_set.table_size

        # Insert elements until rehashing occurs
        inserted_words = []
        for i in range(20):
            word = f"word{i}"
            initial_load = dynamic_set.get_load()
            dynamic_set.insert(word)
            inserted_words.append(word)

            # Check if rehashing occurred
            if dynamic_set.table_size > initial_size:
                print(f"Rehashed at word: {word}")
                print(f"Old size: {initial_size}, New size: {dynamic_set.table_size}")
                print(f"Load before rehash: {initial_load:.2f}")
                print(f"Load after rehash: {dynamic_set.get_load():.2f}")

                # Verify all elements still exist after rehashing
                for w in inserted_words:
                    assert dynamic_set.find(w) == True, f"Lost element {w} after rehashing"
                break

        print(f"Final table: {dynamic_set}")


def test_digital_library():
    print("\nTesting Digital Library Implementation...")

    # Test MuskLibrary
    print("\nTesting MuskLibrary...")
    book_titles = ["booka", "bookb", "bookc"]
    texts = [
        ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog", "quick"],
        ["to", "be", "or", "not", "to", "be", "that", "is", "the", "question"],
        ["all", "that", "glitters", "is", "not", "gold"]
    ]

    musk_lib = MuskLibrary(book_titles, texts)

    # Test distinct words
    for title in book_titles:
        words = musk_lib.distinct_words(title)
        count = musk_lib.count_distinct_words(title)
        print(f"\nDistinct words in {title}: {words}")
        print(f"Count of distinct words: {count}")

    # Test keyword search
    test_keywords = ["the", "is", "not", "nonexistent"]
    for keyword in test_keywords:
        books = musk_lib.search_keyword(keyword)
        print(f"\nBooks containing '{keyword}': {books}")

    print("\nPrinting all books:")
    musk_lib.print_books()

    # Test JGBLibrary
    print("\nTesting JGBLibrary...")
    libraries = [
        ("Jobs", (3, 5)),
        ("Bezos", (3, 5, 7, 11)),
        ("Gates", (3, 5))
    ]

    for name, params in libraries:
        print(f"\nTesting {name} Library:")
        lib = JGBLibrary(name, params)

        # Add books
        lib.add_book("Testa", ["apple", "banana", "apple"])
        lib.add_book("Testb", ["cherry", "date", "cherry"])

        # Test functions
        print("\nPrinting all books:")
        lib.print_books()

        print("\nSearching for 'apple':")
        print(lib.search_keyword("apple"))

        print("\nDistinct words in Testa:")
        lib.distinct_words("Testa")

        print(f"Count of distinct words in Test1: {lib.count_distinct_words('Testa')}")


def run_all_tests():
    print("Starting comprehensive hash table tests...")

    all_tests = [
        ("HashSet Tests", test_hash_set),
        ("HashMap Tests", test_hash_map),
        ("DynamicHashSet Tests", test_dynamic_hash_set),
        ("Digital Library Tests", test_digital_library)
    ]

    for test_name, test_func in progress_bar(all_tests, prefix='Overall Progress:', suffix='Complete', length=50):
        print(f"\n{'=' * 50}\nRunning {test_name}\n{'=' * 50}")
        test_func()
        time.sleep(0.5)


if __name__ == "__main__":
    run_all_tests()