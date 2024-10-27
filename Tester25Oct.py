from library import MuskLibrary

book_titles = ["book1", "book2","book1"]
texts = [["The", "name", "of", "this", "book", "contains", "a", "number"],
         ["You", "can", "name", "this", "book", "anything",'this','can'],
         ["You", "can", "name", "this", "book", "anything",'this','can']]


musk_lib = MuskLibrary(book_titles, texts)
print(musk_lib.mergesort([6,3,5,2,3,10,1]))
# print(musk_lib.distinct_words("book1"))