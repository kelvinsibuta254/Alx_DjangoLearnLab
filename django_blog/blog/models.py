# from django.db import models
# from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin
# from taggit.managers import TaggableManager
# from rest_framework import mixins
# from django.conf import settings


# # Create your models here.

# # class UserManager(BaseUserManager):
# #     def create_user(self, email, password):
# #         if not email:
# #             raise ValueError("email is required")
# #         user = self.model(email = self.normalize_email(email))
# #         user.set_password(password)
# #         user.save(using=self_.db)
# #         return user

# #     def create_superuser(self, email, password):
# #         user = self.create_user(email=email, password=password)
# #         user.is_staff = True
# #         user.is_superuser = True
# #         user.save(using=self._db)
# #         return user

# class PersonManager(BaseUserManager):
#      def create_user(self, email,date_of_birth, username,password=None,):
#          if not email:
#             raise ValueError('Users must have an email address')

#          if not username:
#             raise ValueError('This username is not valid')

#          if not date_of_birth:
#             raise ValueError('Please Verify Your DOB')

#          user = self.model(

#  email=PersonManager.normalize_email(email),username=username,date_of_birth=date_of_birth)

#          user.set_password(password)
#          user.save(using=self._db)
#          return user

#      def create_superuser(self,email,username,password,date_of_birth):
#          user = self.create_user(email,password=password,username=username,date_of_birth=date_of_birth)
#          user.is_admin = True
#          user.is_staff = True
#          user.is_superuser = True
#          user.save(using=self._db)
#          return user


# class Person(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(verbose_name='email address', max_length=255, unique=True, db_index=True,)
#     username = models.CharField(max_length=255, unique=True)
#     date_of_birth = models.DateField()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username', 'date_of_birth',]

#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)

#     objects = PersonManager()

#     def get_full_name(self):
#         return self.email

#     def get_short_name(self):
#         return self.email

#     def __unicode__(self):
#         return self.email

# # class Person(AbstractUser, PermissionsMixin):
# #     email = models.EmailField(unique=True, max_length=255)
# #     username = models.CharField(max_length=20)
# #     objects = UserManager()
# #     USERNAME_FIELD = 'email'
# #     REQUIRED_FIELDS = []



# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     published_date = models.DateTimeField(auto_now_add=True)
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

# class Profile(models.Model):
#     pic = models.URLField()
#     bio = models.TextField(max_length=255)
#     address = models.CharField(max_length=100)
#     country = models.CharField(max_length=50)
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null=True, blank=True)

# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)

# class Tag(models.Model):
#     name = models.ManyToManyField(Post)
#     tags = TaggableManager()

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

# Blog Post 
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
# User Profile
class Profile(models.Model):
       user = models.OneToOneField(User, on_delete=models.CASCADE)
       bio = models.TextField(max_length=500, blank=True)
       location = models.CharField(max_length=30, blank=True)
       birth_date = models.DateField(null=True, blank=True)

       def __str__(self):
           return f'{self.user.username} Profile'
    
# Blog Comment System
class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'