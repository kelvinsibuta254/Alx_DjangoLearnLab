from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission
from rest_framework.views import APIView


# Create your views here.
class BookListAPIView(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

# Create your views here.

class BookViewSet2(viewsets.ViewSet):
    """
    Viewset --> is a class-based view which doesn't provide any method handlers
    for your request

    View --> is a python function or python class that accepts Http request and 
    returns and Http Response
    """
    
    def list(self, request):
        """This is a method instance:
        Returns a list of members"""
        books = Book.objects.all()

        #serialize and deserialize queryset
        serializer = BookSerializer(books, many=True)
        """many=True returns a list of members"""
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        book = Book.objects.filter(pk=pk).first()
        if not book:
            message = {"detail": f"book with id {pk} is not found"}
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    def create(self, request):
        queryset = Book.objects.create(**request.data)
        serializer = BookSerializer(queryset)
        return Response(serializer.data)

    def update(self, request):
        pass

    def partial_update(self, request, pk):
        pass

    def destroy(self, request, pk):
        return Response(status=status.NO_CONTENT)

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class MyAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Only authenticated users can access this view"""
        return Response(
            {"message": "Hello authenticated user!"}
        )
    
class IsAdminOrReadOnly(BasePermission):
    """This is a custom permission class
    Allow read-only access to everyone, but requires the user to be admin (staff) for any write permissions"""
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        return request.user.is_staff
    
class BookListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Only authenticated users can view the list of models"""
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)
    
class BookCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def post(self, request):
        """Only admin users can create new model instances"""
        serializer = BookSerializer
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)