import hash_table as ht

class DigitalLibrary:
    def __init__(self):pass
    def distinct_words(self, book_title):pass
    def count_distinct_words(self, book_title):pass
    def search_keyword(self, keyword):pass
    def print_books(self):pass

class JGBLibrary(DigitalLibrary):
    def __init__(self, name, params):
        super().__init__()
        self.name = name
        if name == "Jobs":
            self.collision_type = "Chain"
            self.params = params
        elif name == "Gates":
            self.collision_type = "Linear"
            self.params = params
        else:
            self.collision_type = "Double"
            self.params = params
        self.books = ht.HashMap(self.collision_type, self.params)
        self.all_book_title_list = []

    def add_book(self, book_title, text):
        book_words = ht.HashSet(self.collision_type, self.params)
        for word in text:
            book_words.insert(word)
        self.books.insert((book_title, book_words))
        self.all_book_title_list.append(book_title)

    def distinct_words(self, book_title):
        book_words = self.books.find(book_title)
        if book_words is None:
            return []
        words = []
        for slot in book_words.table:
            if slot is not None:
                if isinstance(slot, list):
                    words.extend([word for word in slot if word is not None])
                else:
                    words.append(slot)
        return words

    def count_distinct_words(self, book_title):
        book_words = self.books.find(book_title)
        if book_words is None:
            return 0
        return book_words.count

    def search_keyword(self, keyword):
        matching_books = []
        for book_title in self.all_book_title_list:
            book_words = self.books.find(book_title)
            if book_words is not None and book_words.find(keyword):
                matching_books.append(book_title)
        return matching_books

    def print_books(self):
        result = []
        for book_title in self.all_book_title_list:
            book_words = self.books.find(book_title)
            if book_words is not None:
                result.append(f"{book_title}: {str(book_words)}")
        print("\n".join(result))
class MuskLibrary(DigitalLibrary):
    def __init__(self, book_titles, texts):
        super().__init__()

        sorted_pairs = self.mergesort(list(zip(book_titles, texts)), key=lambda x: x[0])
        n_books = len(book_titles)
        self.titles = [None] * n_books
        self.book_words = [None] * n_books
        self.word_counts = [None] * n_books
        i = 0
        for title, text in sorted_pairs:
            self.titles[i] = title
            sorted_words = self.mergesort(list(text))
            self.book_words[i] = sorted_words
            self.word_counts[i] = len(sorted_words)
            i += 1

    def mergesort(self, arr, key=lambda x: x):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.mergesort(arr[:mid], key)
        right = self.mergesort(arr[mid:], key)

        return self.merge(left, right, key)

    def merge(self, left, right, key=lambda x: x):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if key(left[i]) <= key(right[j]):
                if not result or result[-1] != left[i]:
                    result.append(left[i])
                i += 1
            else:
                if not result or result[-1] != right[j]:
                    result.append(right[j])
                j += 1
        for item in left[i:]:
            if not result or result[-1] != item:
                result.append(item)
        for item in right[j:]:
            if not result or result[-1] != item:
                result.append(item)

        return result

    def find_book_index(self, book_title):
        left, right = 0, len(self.titles) - 1

        while left <= right:
            mid = (left + right) // 2
            if self.titles[mid] == book_title:
                return mid
            elif self.titles[mid] < book_title:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def distinct_words(self, book_title):
        idx = self.find_book_index(book_title)
        if idx == -1:
            return []
        return self.book_words[idx]

    def count_distinct_words(self, book_title):
        idx = self.find_book_index(book_title)
        if idx == -1:
            return 0
        return self.word_counts[idx]

    def search_keyword(self, keyword):
        matching_books = []
        for i in range(len(self.titles)):
            words = self.book_words[i]
            left, right = 0, len(words) - 1
            while left <= right:
                mid = (left + right) // 2
                if words[mid] == keyword:
                    matching_books.append(self.titles[i])
                    break
                elif words[mid] < keyword:
                    left = mid + 1
                else:
                    right = mid - 1
        return matching_books

    def print_books(self):
        result = []
        for i in range(len(self.titles)):
            words = self.book_words[i]
            result.append(f"{self.titles[i]}: {' | '.join(words)}")
        print("\n".join(result))
