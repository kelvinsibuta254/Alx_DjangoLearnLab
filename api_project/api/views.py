from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookList(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
