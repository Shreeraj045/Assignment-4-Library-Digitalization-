import hash_table as ht

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
        '''
        name    : "Jobs", "Gates" or "Bezos"
        params  : Parameters needed for the Hash Table:
            z is the parameter for polynomial accumulation hash
            Use (mod table_size) for compression function
            
            Jobs    -> (z, initial_table_size)
            Gates   -> (z, initial_table_size)
            Bezos   -> (z1, z2, c2, initial_table_size)
                z1 for first hash function
                z2 for second hash function (step size)
                Compression function for second hash: mod c2
        '''
        super().__init__()
        self.name = name

        # Determine collision handling type based on name
        if name == "Jobs":
            self.collision_type = "Chain"
            self.z, self.table_size = params
            self.params = (self.z, self.table_size)
        elif name == "Gates":
            self.collision_type = "Linear"
            self.z, self.table_size = params
            self.params = (self.z, self.table_size)
        else:  # Bezos
            self.collision_type = "Double"
            self.z1, self.z2, self.c2, self.table_size = params
            self.params = (self.z1, self.z2, self.c2, self.table_size)

        # Initialize book collection using HashMaps
        self.books = ht.HashMap(self.collision_type, self.params)  # Maps book titles to their HashSets of words
        self.word_to_books = ht.HashMap(self.collision_type, self.params)

    def add_book(self, book_title, text):
        book_words = ht.HashSet(self.collision_type, self.params)

        # Add all words from the text to the book's HashSet
        for word in text:
            # Add word to book's word set
            book_words.insert(word)

            # Update word to books mapping
            existing_books = self.word_to_books.find(word)
            if existing_books :
                print(existing_books)
                existing_books.insert(book_title)
            else:
                # Add book to existing set
                book_set = ht.HashSet(self.collision_type, self.params)
                book_set.insert(book_title)
                self.word_to_books.insert((word, book_set))

        # Store the book's word set in books map
        self.books.insert((book_title, book_words))
    
    def distinct_words(self, book_title):
        book_words = self.books.find(book_title)
        if book_words is None:
            return []

        # Convert HashSet to list by iterating through the table
        distinct_words = []
        for slot in book_words.table:
            if slot is not None:
                if isinstance(slot, list):  # For chaining
                    distinct_words.extend(slot)
                else:  # For linear probing and double hashing
                    distinct_words.append(slot)

        return distinct_words
    
    def count_distinct_words(self, book_title):
        book_words = self.books.find(book_title)
        if book_words is None:
            return 0
        return book_words.count
        pass
    
    def search_keyword(self, keyword):
        books_with_keyword = self.word_to_books.find(keyword)
        if books_with_keyword is None:
            return []

        # Convert HashSet to list
        matching_books = []
        for slot in books_with_keyword.table:
            if slot is not None:
                if isinstance(slot, list):  # For chaining
                    matching_books.extend(slot)
                else:  # For linear probing and double hashing
                    matching_books.append(slot)

        return matching_books
    
    def print_books(self):
        result = []
        # Iterate through the table slots
        for slot in self.books.table:
            if slot is not None:
                if isinstance(slot, list):  # For chaining
                    for book_entry in slot:
                        book_title = book_entry[0]
                        words = self.distinct_words(book_title)
                        result.append(f"{book_title}: {' | '.join(words)}")
                else:  # For linear probing and double hashing
                    book_title = slot[0]
                    words = self.distinct_words(book_title)
                    result.append(f"{book_title}: {' | '.join(words)}")

        return "\n".join(result)


class MuskLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, book_titles, texts):
        super().__init__()
        # Create pairs of titles and texts for sorting
        paired_data = list(zip(book_titles, texts))

        # Sort pairs using generic mergesort
        sorted_pairs = self.mergesort(paired_data, key=lambda x: x[0])

        # Unzip the sorted pairs
        self.titles = []
        sorted_texts = []
        for title, text in sorted_pairs:
            self.titles.append(title)
            sorted_texts.append(text)

        self.book_words = []
        self.word_counts = []

        # Process each book
        for words in sorted_texts:
            # Create a new list with the words to avoid modifying the input
            words_list = list(words)
            # Sort the words
            sorted_words = self.mergesort(words_list, key=str.lower)  # Case-insensitive sort
            # Get distinct words
            distinct = self.get_distinct_words(sorted_words)

            self.book_words.append(distinct)
            self.word_counts.append(len(distinct))

    def get_distinct_words(self, sorted_words):
        if not sorted_words:
            return []

        distinct = [sorted_words[0]]  # Start with the first word

        # Compare each word with the previous distinct word
        for word in sorted_words[1:]:
            if word.lower() != distinct[-1].lower():
                distinct.append(word)

        return distinct
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
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
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
        keyword_lower = keyword.lower()
        for i in range(len(self.titles)):
            words = self.book_words[i]
            # Binary search since words are sorted
            left, right = 0, len(words) - 1
            while left <= right:
                mid = (left + right) // 2
                if words[mid].lower() == keyword_lower:
                    matching_books.append(self.titles[i])
                    break
                elif words[mid].lower() < keyword_lower:
                    left = mid + 1
                else:
                    right = mid - 1
        return matching_books

    def print_books(self):
        result = []
        for i in range(len(self.titles)):
            words = self.book_words[i]
            result.append(f"{self.titles[i]}: {' | '.join(words)}")
        return "\n".join(result)