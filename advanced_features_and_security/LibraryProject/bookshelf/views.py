from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login
from django.contrib.auth.models import Group
from .models import Post
from .forms import CustomUserCreationForm, PostForm
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
        form = PostForm(request.POST)
        if form.is_valid():
            posts = form.save(commit=False)
            posts.author = request.user
            posts.save()
            return redirect("list_posts")
    else:
        form = PostForm()
        return render(request, "blog/create_post.html", {"form": form})
@login_required
@permission_required("blog.edit", raise_exception=True)
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("list_posts")
    else:
        form = PostForm(instance=post)
    return render(request, "blog/edit_post.html", {"form": form})

@login_required
@permission_required("blog.delete_post", raise_exception=True)
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("list_posts")
    return render(request, "blog/delete_post.html", {"post": post})
