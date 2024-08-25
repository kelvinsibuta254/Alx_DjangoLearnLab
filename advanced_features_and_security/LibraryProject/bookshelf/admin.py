from django.contrib import admin
from .models import Book, CustomUser, CustomUserManager
from django.contrib.auth.admin import UserAdmin as CustomUserAdmin

class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')

#Register your models here.
admin.site.register(Book, BookAdmin)

class ModelAdmin(CustomUserManager):
    list_display = ("email", "is_staff")
    

admin.site.register(CustomUser, CustomUserAdmin)
#admin.site.register(ModelAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Post
# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("age",)}),
    
    )
admin.site.register(CustomUser, CustomUserAdmin)

class CustomPostAdmin(admin.ModelAdmin):
    model = Post
    fields = ("title", "author", "content", )

admin.site.register(Post, CustomPostAdmin)
    
