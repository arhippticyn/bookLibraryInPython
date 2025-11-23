from user import User
from book import Book
from librarian import Librarian
from bookFilter import FilterByAuthor
from bookFilter import FilterByYear
from bookFilter import FilterByAvailble
from libraryStorage import LibraryStorage

library = LibraryStorage()

user = User('Arhip', 'Arhip@email.com')
librarian = Librarian('Sony', 'Sony@email.com')

book_1 = Book('Harry Potter', 'Joan Rouling', 1999)
book_2 = Book('Федько Халамидник', 'Volodymir Vunnuchenko', 1823)

library.add_book(book_1)
library.add_book(book_2)

filter_author = FilterByAuthor('Joan Rouling')
results = filter_author.apply(library.list_all())

for result in results:
    print(result.info())