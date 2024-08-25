from django.contrib import admin
from .models import Librarian

class BookAdmin(admin.ModelAdmin):
    list_filter = ('name', 'library')
    search_fields = ('name', 'library')

# Register your models here.
admin.site.register(Librarian, BookAdmin)