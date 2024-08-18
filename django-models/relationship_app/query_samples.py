from .models import Book

#Filtering books by author
book_by_author = Book.objects.filter(author="George Orwel")
