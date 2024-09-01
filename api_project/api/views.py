from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewset(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

# Create your views here.
# class BookListAPIView(generics.ListAPIView):
#     serializer_class = BookSerializer
#     queryset = Book.objects.all()