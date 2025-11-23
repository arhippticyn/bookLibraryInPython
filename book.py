class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_taken = False
        
    def info(self):
        return f'Book {self.title}, Author: {self.author}, year: {self.year}, taken: {self.is_taken}'
    
    def take(self):
     if not self.is_taken:
        self.is_taken = True
        return "Book taken"
     return "Already taken"

        
    def return_book(self):
     if self.is_taken:
        self.is_taken = False
        return "Book returned"
     return "Book was not taken"
