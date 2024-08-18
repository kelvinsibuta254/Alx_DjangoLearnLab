from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library

# Create your views here.

def index(request):
    return HttpResponse("Hello there! Welcome to my Library. How may I help you?")

def book_list(request):
    books = Book.objects.all()
    context = {"book_list": books}
    return render(request, 'books/book_list.html', context)
    

# class Hello_view(TemplateView):
#     template_name = "hello.html"

class LibraryDetailView(DetailView):
    model = Library
    template_name = "books/book_detail.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        library = self.get_object()
        context["average_rating"] = library.get_average_rating()

# class BookUpdateView(UpdateView):
#     model = Book
#     fields = ["title", "author"]
#     template_name = "books/book_update_form.html"
#     success_url = reverse_lazy("book_list")

#     def form_valid(self, form):
#         response = super().form_valid(form)
#         return response

