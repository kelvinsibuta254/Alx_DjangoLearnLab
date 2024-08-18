from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("book/", views.book_list, name="book"),
    path("library/", views.LibraryDetailView.as_View(), name="library")
]