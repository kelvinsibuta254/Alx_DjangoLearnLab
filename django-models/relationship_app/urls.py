from django.urls import path
from .views import admin_view, librarian_view, member_view
from . import views
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView
from .views import CustomLogoutView
from .views import register


urlpatterns = [
    path('admin/', admin_view, name='admin'),
    path('librarian/', librarian_view, name='librarian'),
    path('member/', member_view, name='member'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    # path('logout/', LogoutView.as_view(template_name='relationship_app/simple_logout.html'), name='logout'),
    path('logout/', CustomLogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('books/', views.list_books, name='books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('add_book/', views.can_add_book),
    path('edit_book/', views.can_change_book),
    path('delete_book', views.can_delete_book),
]