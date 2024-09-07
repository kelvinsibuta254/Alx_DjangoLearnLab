# api/urls.py

from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    # List and Detail views (already existing)
    path('books/create', BookCreateView.as_view(), name='book-create'),
    path('books/list', BookListView.as_view(), name='book-list'),
    path('books/update', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/delete', BookDeleteView.as_view(), name='book-delete'),

    # Create, Update, and Delete views
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),
    path('books/update/', views.BookUpdateView.as_view(), name='book-update'),
    path('books/delete/', views.BookDeleteView.as_view(), name='book-delete'),
]