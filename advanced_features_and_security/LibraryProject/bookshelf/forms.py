from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser, Post

class CustomUserCreationForm(UserCreationForm):
    ROLES = [
        ("creator", "Creator"),
        ("reader", "Reader"),
    ]
    role = forms.ChoiceField(choices=ROLES, required=True)
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fileds = UserCreationForm.Meta.fields + (
            "email", "age", "role"
        )

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]