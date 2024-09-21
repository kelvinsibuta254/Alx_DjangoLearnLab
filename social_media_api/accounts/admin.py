from django.contrib import admin
from django.contrib.auth.admin import  UserAdmin as DefaultAdmin
from .models import CustomUser, Post

# Register models
admin.site.register(CustomUser)
admin.site.register(Post)