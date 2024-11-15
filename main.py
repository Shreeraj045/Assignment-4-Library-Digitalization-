import library
import hash_table
from prime_generator import set_primes


def get_primes(start=10 ** 3, end=10 ** 5):
    is_prime = [True] * (end + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, end + 1):
        if not is_prime[i]: continue

        for j in range(2 * i, end + 1, i):
            is_prime[j] = False

    prime_sizes = []
    sz = start
    while sz <= end:
        if not is_prime[sz]:
            sz += 1
            continue

        prime_sizes.append(sz)
        sz *= 2

    prime_sizes.reverse()
    return prime_sizes


def main():
    book_titles = ["booka", "bookb", "bookaa", "bookaaa"]
    texts = [["x"],
             ["x"],
             ["x"],
             ["x"]
             ]

    unique_words = []

    for text in texts:
        unique = []
        for word in text:
            if word not in unique:
                unique.append(word)
        unique_words.append(sorted(unique))

    word_to_books = {}

    for book, text in zip(book_titles, texts):
        for word in text:
            if word not in word_to_books:
                word_to_books[word] = [book]
            else:
                word_to_books[word].append(book)

    set_primes(get_primes())

    # Check Musk
    musk_lib = library.MuskLibrary(book_titles, texts)
    jobs_lib = library.JGBLibrary("Jobs", (10, 29))
    gates_lib = library.JGBLibrary("Gates", (10, 37))
    bezos_lib = library.JGBLibrary("Bezos",
                                   (10, 37,
                                    7, 13)
                                   )

    for lib, name in zip([jobs_lib, gates_lib, bezos_lib], ["Jobs", "Gates", "Bezos"]):
        for book, text in zip(book_titles, texts):
            lib.add_book(book, text)

    print("jobs", jobs_lib.books.__str__())
    print()
    print("gates", gates_lib.books.__str__())
    print()
    print("bezos", bezos_lib.books.__str__())


if __name__ == "__main__":
    main()