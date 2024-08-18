from .models import Book, Library

#Filtering books by author
book_by_author = Book.objects.filter(author="George Orwel")

Library.objects.get(name = library_name)

#Listing all books
books = Book.objects.all()
