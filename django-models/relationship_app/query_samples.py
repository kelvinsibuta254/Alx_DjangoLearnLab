from .models import Author, Book, Library, Librarian

#Creating author field
Wilson = Author.objects.create(name="Wilson Rawls")
Wilson.save()

#Querying all books by a specific author
#Wilson = Author.objects.get(name="Wilson Rawls")
Author.objects.filter(author = Wilson)
Author.objects.filter(author=Wilson)
#Adding titles of the Book
Last = Book.objects.create(title="All the Wrong Questions: When Did you See Her Last?")
Last.save()
#Filtering books by author
Book.objects.get(author=Wilson)

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
