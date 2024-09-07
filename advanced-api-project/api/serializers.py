from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class AuthorSerializer(serializers.ModelSerializer):
    book = BookSerializer(many=True, read_only=True)
    "Serializes the author's name and related books"
    class Meta:
        model = Author
        fields = ["name", "book"]""

    def validate_publication_year(self, value):
        current_year = date.today().year
        if year > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return year