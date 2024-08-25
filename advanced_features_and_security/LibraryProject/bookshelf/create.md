# This command creates the book instance with the title, author and the year of publication

# Command
book1 = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

book1.save()

# Output
This command outputs an empty list on a command shell. However, when retrieving the book from bookshelf database using mysql, you get the title of the book, author and publication year.
