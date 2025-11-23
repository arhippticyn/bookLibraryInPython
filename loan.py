from abc import ABC, abstractmethod

class Sender(ABC):
    @abstractmethod
    def send(self, msg):
        pass
    
class EmailSender(Sender):
    def send(self, msg):
        return f'Email message: {msg}'
    
class SmsSender(Sender):
    def send(self, msg):
        return f'SMS message: {msg}'
    
class LoanManager:
    def __init__(self, storage, sender):
        self.storage = storage
        self.sender = sender
        
    def loan_book(self, user, book_title):
        book = self.storage.find_by_title(book_title)
        if not book:
            return 'Book is not found'
        
        result = book.take()
        
        if result == 'Already taken':
            return 'Book already taken'
        
        self.sender.send(f'Book {book_title} is loaned to {user.get_name()}')
        
        return self.sender.send(f'Book {book_title} is loaned to {user.get_name()}'), 'loan is succes'
        # print(self.sender)
        # print(f"Book {book_title} is loaned to {user.name}")
    
    def return_book(self, book_title):
        book = self.storage.find_by_title(book_title)
        if not book:
            return 'Book is not found'
        
        result = book.return_book()
        
        self.sender.send(f'book {book_title} is returned')
        
        return self.sender.send(f'book {book_title} is returned'), result
