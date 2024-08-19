from django.shortcuts import render, redirect
from .models import Book
from django.contrib.auth.decorators import permission_required
from django.views.generic.detail import DetailView
from .models import Library
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from . import BookForm

from django.shortcuts import render, redirect
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView, LogoutView

# Function-based View
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-based View
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')  # Redirect to a view after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    

from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserProfile


def is_admin(user):
    return user.is_authenticated and user.UserProfile.role=="Admin"

def Librarian(user):
    return user.role == "Librarians"

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role==" Librarian "

def is_member(user):
    return user.is_authenticated and user.UserProfile.role=="Member"


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

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


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


# Class-based View
# class LibraryDetailView(DetailView):
#     model = Library
#     template_name = 'relationship_app/library_detail.html'
#     context_object_name = 'library'


# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('list_books')  # Redirect to a view after registration
#     else:
#         form = UserCreationForm()
#     return render(request, 'relationship_app/register.html', {'form': form})


# class CustomLogoutView(LogoutView):
#     def get(self, request, *args, **kwargs):
#         return self.post(request, *args, **kwargs)


# def Admin(user):
#     return user.is_authenticated and user.userprofile.role == 'Admin'

# @user_passes_test(Admin)
# def admin_view(request):
#     return render(request, template_name='relationship_app/admin_view.html')

# @login_required
# @user_passes_test(Admin)
# def Admin(request):
#     return render(request, template_name='relationship_app/admin_view.html')

# def Librarian(user):
#     return user.is_authenticated and user.role == "Librarians"

# @user_passes_test(Librarian)
# def librarian_view(request):
#     return render(request, template_name='relationship_app/librarian_view.html')

# @login_required
# @user_passes_test(Librarian)
# def librarian_view(request):
#     return render(request, template_name='relationship_app/librarian_view.html')

# def Member(user):
#     return user.is_authenticated and user.userprofile.role == 'Member'

# @user_passes_test(Member)
# def member_view(request):
#     return render(request, template_name='relationship_app/member_view.html')

# @login_required
# @user_passes_test(Member)
# def member_view(request):
#     return render(request, template_name='relationship_app/member_view.html')