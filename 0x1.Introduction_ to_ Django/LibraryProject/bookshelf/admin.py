from django.contrib import admin

from .models import Book

admin.ModelAdmin

# Register your models here.

admin.site.register(Book)
