from django.contrib.auth.forms import UserCreationForm as DefaultForm
from django import forms
from django.contrib.auth.models import User
from .models import Post

class UserCreationForm(DefaultForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = '__all__'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(PostForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        post = super(PostForm, self).save(commit=False)
        if self.user and not post.pk:
            post.author = self.user
        if commit:
            post.save()
        return post