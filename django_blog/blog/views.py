from typing import Any
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm, CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView
from .models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from rest_framework import generics

def register(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog/login.html')  
        
        form = CustomUserForm()
        context = {'form': form}
        return render(request, 'blog/register.html', context_instance = RequestContext(request))

def login(request):     
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = form.authenticate(
                                    username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('blog/base.html')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)

    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'blog/login.html', context)

@login_required
def customlogout(request):
    logout(request)
    return redirect('blog/base.html')

def home(request):
    return render(request, 'blog/base.html')

@login_required
def profile(request):
    return render(request, 'blog/profile.html')

def user_profile(request):
    """Displays information unique to the logged-in user."""

    user = authenticate(username='superuserusername', password='sueruserpassword')
    login(request, user)

class Post(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/post_list.html'

    def get_gueryset(self):
        return Post.objects.all()
    
class postdetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class postcreate(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class postupdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = PostForm
    template_name = 'blog/post_update.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(author=self.request.user)
    
class postdelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'

    def test_func(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(author=self.request.user)
    
class CommentCreateView(LoginRequiredMixin, CreateView):
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = CommentForm
    template_name = 'blog/comment_update_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
    def test_func(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(author=self.request.user)
    
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def test_func(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(author=self.request.user)
    
class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/posts_by_tag.html'

    def get_queryset(self):
        tag_name = self.kwargs.get('name')
        tag = get_object_or_404(Tag, name=tag_name)
        return Post.objects.filter(tags=tag)


class SearchResultView(ListView):
    model =Post
    template_name = 'blog/post_search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        )

class Edit(PermissionRequiredMixin):
    permission_required = ('posts.can_open', 'posts.can_edit')

    # View