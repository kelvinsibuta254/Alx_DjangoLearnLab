from django.shortcuts import render, redirect
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

from django.contrib.auth.decorators import login_required, user_passes_test

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


def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, template_name='relationship_app/admin_view.html')

def Librarian(user):
    return user.is_authenticated and user.userprofile.role=='Librarians'

@user_passes_test(Librarian)
def Librarianview(request):
    return render(request, template_name='relationship_app/librarian_view.html')

def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'

@user_passes_test(is_member)
def Memberview(request):
    return render(request, template_name='relationship_app/member_view.html')

@login_required
@user_passes_test(is_admin)
def Adminview(request):
    return render(request, template_name='relationship_app/admin_view.html')

@login_required
@user_passes_test(Librarian)
def Librarianview(request):
    return render(request, template_name='relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member)
def Memberview(request):
    return render(request, template_name='relationship_app/member_view.html')