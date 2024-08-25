from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login
from django.contrib.auth.models import Group
from .models import Post
from .forms import ExampleForm

from .forms import CustomUserCreationForm
# Create your views here.

def index(request):
    return HttpResponse("Hello there! Welcome to my Library. How may I help you?")

# Create your views here.
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data.get("role")
            if role == "creator":
                creator_group = Group.objects.get(name="Creator")
                user.groups.add(creator_group)
            elif role == "reader":
                creator_group = Group.objects.get(name="Reader")
                user.groups.add(creator_group)
            login(request, user)
            return redirect("list_posts")
    else:
        form = CustomUserCreationForm()
    return render(request, "blog/register.html", {"form": form})

def list_posts(request):
    posts = Post.objects.all()
    return render(request, "blog/list_posts.html", {"posts": posts})

@login_required
@permission_required("blog.create", raise_exception=True)
def create_post(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            posts = form.save(commit=False)
            posts.author = request.user
            posts.save()
            return redirect("list_posts")
    else:
        form = ExampleForm()
        return render(request, "blog/create_post.html", {"form": form})
@login_required
@permission_required("blog.edit", raise_exception=True)
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = ExampleForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("list_posts")
    else:
        form = ExampleForm(instance=post)
    return render(request, "blog/edit_post.html", {"form": form})

@login_required
@permission_required("blog.delete_post", raise_exception=True)
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("list_posts")
    return render(request, "blog/delete_post.html", {"post": post})

from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic import View
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.forms import UserCreationForm
from .forms import BookForm

from .models import Book, UserProfile
from .models import Library

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


def index(request):
    return render(request, 'relationship_app/index.html')


def list_books(request):
    items = Book.objects.all()
    book_list = [f"{i.title} by {i.author}" for i in items]
    return render(request, "relationship_app/list_books.html", {"book_list": book_list})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['library'] = self.object
        return context

def check_admin(user):
    return user.userprofile.role == 'Admin'

@user_passes_test(check_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')  

#Check for Librarian
def check_librarian(user):
    return user.userprofile.role == 'Librarian'

@user_passes_test(check_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

#Checking if member exists
def check_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(check_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")

@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_all_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.can_change_book')
def change_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_all_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/change_book.html', {'form': form, 'book': book}) 


@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.methon == 'POST':
        book.delete()
        return redirect('list_all_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})
