class LibraryStorage:
    def __init__(self):
        self.library = []
        
    def add_book(self, book):
        self.library.append(book)
        
    def remove_book(self, book):
        self.library.remove(book)
        
    def find_by_title(self, title):
        for book in self.library:
            if book.title == title:
                return book
        
    def list_all(self):
        return self.library