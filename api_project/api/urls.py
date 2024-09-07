from .views import BookListAPIView, BookViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     path('books/', BookListAPIView.as_view(), name='book-list'),
#     path('api/', include('api.urls'))
#     ]

# router = DefaultRouter()
# router.register('api/', BookViewSet, basename='api')
# urlpatterns = router.urls


from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from .views import BookCreateView, BookListView, BookRetrieveView, CustomBookCreateView, BookList, CustomBookListView, BookViewSet, RetrieveBookView, BaseRetrieveView, BaseRetrieveUpdateDestroyView
from django.urls import path
from .models import Book
from .serializers import BookSerializer

router = DefaultRouter()
"""router returns a list of urlpatterns"""

router.register("GeneBook", GeneBankViewSet, basename="GeneBook")

urlpatterns = router.urls
urlpatterns = [
    path('book/create', BookCreateView.as_view(queryset=Book.objects.all(), serializer_class=BookSerializer), name='book-create'),
    path('book/', CustomBookCreateView.as_view(queryset=Book.objects.all(), serializer_class=BookSerializer), name='create-list'),
    path('book/list', CustomBookListView.as_view(queryset=Book.objects.all(), serializer_class=BookSerializer), name='book-list'),
    path('booklist/', BookListView.as_view(queryset=Book.objects.all(), serializer_class=BookSerializer), name='booklist'),
    path('book/retrieve', RetrieveBookView.as_view(queryset=Book.objects.all(), serializer_class=BookSerializer), name='book-retrieve'),
    path('bookretrieve/', BookRetrieveView.as_view(queryset=Book.objects.all(), serializer_class=BookSerializer), name='book-detail'),
    #path('gene/<int:pk>/', GeneBankRetrieveView.as_view(queryset=GeneBank.objects.all(), serializer_class=GeneBankSerializer), name='gene-retrieve'),

    ]