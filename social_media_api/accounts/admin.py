from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import  UserAdmin as DefaultAdmin
from .models import User, Post
# Register your models here.

class UserAdmin(DefaultAdmin):
    model = User
    fieldsets = DefaultAdmin.fieldsets + (
        (None, {"fields": ("age",)}),
    
    )

admin.site.register(User, UserAdmin)
admin.site.register(Post)