from abc import ABC, abstractmethod

class BookFilter(ABC):
    @abstractmethod
    def apply(self, books):
        pass
    
class FilterByAuthor(BookFilter):
    def __init__(self, author):
        self.author = author
        
    def apply(self, books):
        return [book for book in books if book.author == self.author]
        
class FilterByYear(BookFilter):
    def __init__(self, year):
        self.year = year
        
    def apply(self, books):
        return [book for book in books if book.year == self.year]
    
class FilterByAvailble(BookFilter):
    def __init__(self, availble):
        self.availble = availble
        
    def apply(self, books):
        return [ book for book in books if not book.is_taken]