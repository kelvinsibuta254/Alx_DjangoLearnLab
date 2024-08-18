## create.md

# This command creates the book instance with the title, author and the year of publication

# Command
book1 = Book(title="1984", author="George Orwell", publication_year=1949)

book1.save()

# Output
This command outputs an empty list on a command shell. However, when retrieving the book from bookshelf database using mysql, you get the title of the book, author and publication year.



## Retrive.md

# This command retrieve all attribute of the book1 created

# Command
Book.objects.all()

# Output
<QuerySet [<Book: Book object (1)>]>



## Update.md

# This command updates the title of book1 from "1984" to "Nineteen Eighty-Four" and save the changes

# command
book1.title = "Nineteen Eighty-Four"

book1.save()

# Output
When retrieving book1 from mysql, you will notice that the title of the book has changed from "1984" to "Nineteen Eighty-Four"


## Delete.md

# This command deletes the book1 from bookshelf database

# command
Book.delete(book1)

# Output
(1, {'bookshelf.Book' : 1})