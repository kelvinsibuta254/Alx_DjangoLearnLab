# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views.generic import DetailView
# from .models import Book, Library

# # Create your views here.

# def index(request):
#     return HttpResponse("Hello there! Welcome to my Library. How may I help you?")

# def book_list(request):
#     books = Book.objects.all()
#     context = {"book_list": books}
#     return render(request, 'books/book_list.html', context)
    

# # class Hello_view(TemplateView):
# #     template_name = "hello.html"

# class LibraryDetailView(DetailView):
#     model = Library
#     template_name = "books/book_detail.html"

#     def get_context_data(self, **kwargs):
#         context =  super().get_context_data(**kwargs)
#         library = self.get_object()
#         context["average_rating"] = library.get_average_rating()

# # class BookUpdateView(UpdateView):
# #     model = Book
# #     fields = ["title", "author"]
# #     template_name = "books/book_update_form.html"
# #     success_url = reverse_lazy("book_list")

#     # def form_valid(self, form):
#     #     response = super().form_valid(form)
#     #     return response
# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login
# # relationship_app/views.py
# from django.contrib.auth.views import LoginView
# # relationship_app/views.py
# from django.contrib.auth.views import LogoutView

# class CustomLoginView(LoginView):
#     template_name = 'relationship_app/login.html'
# class CustomLogoutView(LogoutView):
#     template_name = 'relationship_app/logout.html'    

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')  # Adjust 'home' to your desired redirect URL
#     else:
#         form = UserCreationForm()
#     return render(request, 'relationship_app/register.html', {'form': form})

# relationship_app/views.py
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

# Helper functions to check user roles
def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'
    # return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

# Views
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')



from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render


def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')



# relationship_app/views.py
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from . import BookForm  # Assuming you have a form for Book

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Adjust 'book_list' to your desired redirect URL
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=book.id)  # Adjust as needed
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Adjust as needed
    return render(request, 'relationship_app/delete_book.html', {'book': book})


