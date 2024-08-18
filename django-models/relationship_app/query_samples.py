from .models import Author, Book, Library, Librarian

#Creating author field
author_name = Author.objects.create(name="Wilson Rawls")
author_name.save()
author = "Wilson Rawls"

#Querying all books by a specific author
Author.objects.get(name=author_name)
Author.objects.filter(author=author)

#Adding titles of the Book
Last = Book.objects.create(title="All the Wrong Questions: When Did you See Her Last?")
Last.save()
#Filtering books by author
Book.objects.get(author=author_name)

#Library
Sibuta = Library.objects.create(name="Sibuta")

#Adding Books to the Library
Sibuta.books.add(Last)

#Listing all books in a Library
Sibuta.books.all()
Sibuta.objects.get(name=Sibuta)

#Adding a Librarian
kssibuta = Librarian.objects.create(name="KSSibuta", library=Sibuta)
kssibuta.save()

kssibuta.library

#Retrieving a Librarian
Librarian.objects.get(library= Sibuta)

#Listing all books
books = Book.objects.all()
