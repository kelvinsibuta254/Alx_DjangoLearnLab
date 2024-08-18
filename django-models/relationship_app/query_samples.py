from .models import Author, Book, Library, Librarian

#Creating author field
author_name = Author.objects.create(name="Wilson Rawls")
author_name.save()

#Querying all books by a specific author
#Wilson = Author.objects.get(name="Wilson Rawls")
author = Author.objects.filter(author = author_name)
#Adding titles of the Book
Last = Book.objects.create(title="All the Wrong Questions: When Did you See Her Last?")
Last.save()
#Filtering books by author
book_by_author = Author.objects.get(author=author)

#Library
Sibuta = Library.objects.create(name="Sibuta")

#Adding Books to the Library
Sibuta.books.add(Last)

#Listing all books in a Library
Sibuta.books.all()
Sibuta.objects.get(name=Sibuta)
#Library.objects.get(name=library_name)

#Adding a Librarian
kssibuta = Librarian.objects.create(name="KSSibuta", library=Sibuta)
kssibuta.save()

#Retrieving a Librarian
kssibuta.library

#Listing all books
books = Book.objects.all()
