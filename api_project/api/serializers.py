from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

from rest_framework import serializers
from datetime import datetime
from .models import GeneBank

class Book:
    """This is a blueprint for creating Book instances/objects"""
    def __init__(self, title, author, created = None):
        self.title = title
        self.author = author
        self.created = created or datetime.now()

book = Book(title="", author="") # This is an instance.

class BookSerializer(serializers.Serializer):
    
    """This is a custom serializer. It serializes a book object on line 20"""
    title = serializers.CharField()
    author = serializers.CharField(max_length=50)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        """This logic is commonly applied at workplaces"""
        return Book(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title")
        instance.author = validated_data.get("author")
        instance.created = validated_data.get("created")
        return instance