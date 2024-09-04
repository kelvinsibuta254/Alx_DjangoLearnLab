from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

class Book:
    """This is a blueprint for creating book instances/objects"""
    def __init__(self, title, publication_year=None):
        self.title = title
        self.publication_year = publication_year or datetime.now()

book = Book(title="When did you see her last?", publication_year=1990)

class BookSerializer(serializers.Serializer):
    title = serializers.CharField()
    publication_year = serializers.IntegerField()
    # class Meta:
    #     model = Book
    #     fields = "__all__"

class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField()
    
    # class BookSerializer(serializers.Serializer):
    #     name = serializers.RelatedField(Author)
    # class Meta:
    #     model = Author
    #     fields = "__all__"