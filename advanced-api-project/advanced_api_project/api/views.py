from django.shortcuts import render
from django.urls import path
# from .views import  UserViewSet
from rest_framework import generics, viewsets
from rest_framework.routers import DefaultRouter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Book, BookSerializer, Author, AuthorSerializer

@api_view(['GET'])
def hello_world(request):
    """This decorator allows a function to be accessed using HTTP"""
    #instance
    book = Book(title="when did you see her last?", publication_year=1990)
    serializer = BookSerializer(book)
    """This serializes your instance"""
    
    #Deserialize
    serializer2 = BookSerializer(data = serializer.data)
    if serializer2.is_valid():
        print(f"DESERIALIZED \n {serializer2.validated_data}")
    print(serializer.data)
    return Response({"data": "serializer.data"})

# router = DefaultRouter()
# """router returns a list of urlpatterns"""

# router.register("api", UserViewSet, basename="api")

# urlpatterns = router.urls

class BookViewset(viewsets.ViewSet):
    #queryset = Book.objects.all()
    serializer_class = BookSerializer

    def create(self, validated_data):
        """This logic is commonly applied at workplaces"""
        # return Comment(
        #     email=validated_data.get("email"),
        #     content=validated_data.get("content"),
        #     created=validated_data.get("created"),
        # )
        return Book(**validated_data)
    
    def update(self, instance, validated_data):
        instance.email = validated_data.get("email")
        instance.content = validated_data.get("content")
        instance.created = validated_data.get("created")
        return instance