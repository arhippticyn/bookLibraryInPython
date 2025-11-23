from user import User

class Librarian(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        
    # def add_book(self, book):
    #     self.librain.append(book)
        
    # def remove_book(self, book):
    #     self.librain.remove(book)