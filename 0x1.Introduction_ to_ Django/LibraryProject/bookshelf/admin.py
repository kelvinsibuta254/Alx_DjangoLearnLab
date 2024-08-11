admin.site.register(Book)

from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'author')

# Register your models here.
admin.site.register(Book, BookAdmin)
