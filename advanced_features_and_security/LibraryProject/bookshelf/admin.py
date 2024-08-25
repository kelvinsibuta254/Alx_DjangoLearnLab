from django.contrib import admin
from .models import Book, CustomUser, CustomUserManager
from django.contrib.auth.admin import UserAdmin as CustomUserAdmin

class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')

#Register your models here.
admin.site.register(Book, BookAdmin)

class ModelAdmin(CustomUserAdmin):
    list_display = ("email", "is_staff")
    

admin.site.register(CustomUser, CustomUserManager)
admin.site.register(ModelAdmin)

