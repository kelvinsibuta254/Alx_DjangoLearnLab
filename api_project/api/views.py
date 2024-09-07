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


from rest_framework, import mixins, generics
# Mixin - reusable optional actions
# Actions- list, retrieve, update, create
# mixins don't have .get() and .post methods
class BookUserCreateView(mixins.CreateModelMixin, generics.GenericAPIView):
    pass


# This code was added today

from django.shortcuts import render
from rest_framework import generics, mixins
from .models import GeneBank
from rest_framework import viewsets
from .serializers import GeneBankSerializer
from rest_framework.permissions import IsAdminUser

# Create your views here.

class CustomBookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Overrides the view and set several classes
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]

    def list(self, request):
        # Note the use of 'get_queryset()' instead of 'self.queryset'
        queryset = self.get_queryset()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

class BookCreateView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class BookListView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
# Used for get requests
    def get(self, request, *args, **kwargs): # args pass positional arguments to the view
        return self.list(request, *args, **kwargs)

class BookRetrieveView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class CustomBookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

from django.contrib.auth.mixins import LoginRequiredMixin

class MyView(LoginRequiredMixin):
    """Makes sure that people must login to access this view"""
    login_url = '/login/' # define a url someone is going to be redirected to when they are not logged in
    redirect_field_name = 'redirect_to'
    
    def get(self, request):
        """This is a get request for one item or list of items"""
        pass


from .mixins import MultipleFieldLookupMixin, AllowPUTAsCreateMixin

class RetrieveBookView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class =  BookSerializer
    lookup_fields = '__all__'

class BaseRetrieveView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_fields = '__all__'

class BaseRetrieveUpdateDestroyView(MultipleFieldLookupMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_fields = ['title', 'author']