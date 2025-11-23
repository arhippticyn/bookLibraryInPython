class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_taken = False
        
    def info(self):
        return f'Book {self.title}, Author: {self.author}, year: {self.year}, taken: {self.is_taken}'
    
    def take(self):
        if self.is_taken:
            return 'Book taken'
        else:
            return 'Already taken'
        
    def return_book(self):
        if not self.is_taken:
            return 'Book returned'
        else:
            return 'book was not taken'