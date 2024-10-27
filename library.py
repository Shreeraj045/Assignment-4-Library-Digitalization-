import hash_table as ht
import dynamic_hash_table as dht

class DigitalLibrary:
    # DO NOT CHANGE FUNCTIONS IN THIS BASE CLASS
    def __init__(self):
        pass
    
    def distinct_words(self, book_title):
        pass
    
    def count_distinct_words(self, book_title):
        pass
    
    def search_keyword(self, keyword):
        pass
    
    def print_books(self):
        pass
    


class JGBLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, name, params):
        super().__init__()
        self.name = name
        if name == "Jobs":
            self.collision_type = "Chain"
            self.z, self.table_size = params
            self.params = (self.z, self.table_size)
        elif name == "Gates":
            self.collision_type = "Linear"
            self.z, self.table_size = params
            self.params = (self.z, self.table_size)
        else:
            self.collision_type = "Double"
            self.z1, self.z2, self.c2, self.table_size = params
            self.params = (self.z1, self.z2, self.c2, self.table_size)

        self.books = dht.DynamicHashMap(self.collision_type, self.params)
    def add_book(self, book_title, text):
        book_words = dht.DynamicHashSet(self.collision_type, self.params)
        for word in text:
            book_words.insert(word)
        self.books.insert((book_title, book_words))

    def distinct_words(self, book_title):
        book_words = self.books.find(book_title)
        if book_words is None:
            return []
        words = []
        # print("BOOKSSSSS",book_words)
        for slot in book_words.table:
            if slot is not None:
                if isinstance(slot, list):  # For chaining
                    words.extend([word for word in slot if word is not None])
                else:  # For linear/double hashing
                    words.append(slot)
        return [word for word in words if word is not None]
    
    def count_distinct_words(self, book_title):
        book_words = self.books.find(book_title)
        if book_words is None:
            return 0
        return book_words.count

    def search_keyword(self, keyword):
        matching_books = []
        for slot in self.books.table:
            if slot is None:
                continue
            if isinstance(slot, list):  # Chain collision handling
                for book_entry in slot:
                    if book_entry is not None:
                        book_title, word_set = book_entry
                        if word_set.find(keyword):
                            matching_books.append(book_title)
            else:  # Linear/Double collision handling
                if slot is not None:
                    book_title, word_set = slot
                    if word_set.find(keyword):
                        matching_books.append(book_title)

        return [book for book in matching_books if book is not None]
    
    def print_books(self):
        result = []
        for slot in self.books.table:
            if slot is None:
                continue
            if self.collision_type == "Chain" and isinstance(slot, list):
                for entry in slot:
                    book_title = entry[0]
                    book_words = entry[1]
                    result.append(f"{book_title}: {str(book_words)}")
            else:
                if slot is not None:  # For linear probing and double hashing
                    book_title = slot[0]
                    book_words = slot[1]
                    result.append(f"{book_title}: {str(book_words)}")
        print("\n".join(result))


class MuskLibrary(DigitalLibrary):
    def __init__(self, book_titles, texts):
        super().__init__()
        paired_data = list(zip(book_titles, texts))

        sorted_pairs = self.mergesort(paired_data, key=lambda x: x[0])

        self.titles = []
        sorted_texts = []
        for title, text in sorted_pairs:
            self.titles.append(title)
            sorted_texts.append(text)

        self.book_words = []
        self.word_counts = []

        for words in sorted_texts:
            words_list = list(words)
            sorted_words = self.mergesort(words_list)
            self.book_words.append(sorted_words)
            self.word_counts.append(len(sorted_words))
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
                if not result or result[-1] != left[i]:  # Append only if unique
                    result.append(left[i])
                i += 1
            else:
                if not result or result[-1] != right[j]:  # Append only if unique
                    result.append(right[j])
                j += 1

            # Add remaining items, ensuring they are distinct
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