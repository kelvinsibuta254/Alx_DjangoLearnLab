# This command deletes the book1 from bookshelf database
from bookshel.models import Book
# command
Book.delete(book)

# Output
(1, {'bookshelf.Book' : 1})