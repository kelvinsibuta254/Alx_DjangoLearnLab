from django.db import models

from django.db.models.signals import post_save
from django.dispatch import Signal, receiver

from django.contrib.auth.models import User


# Author Model definition
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Book Model definition
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__(self):
        return self.title


# Library Model definition
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


# Librarian Model definition
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ("Admin", "Admin"),
        ("Librarian", "Librarians"),
        ("Member", "Member"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"


@receiver(post_save, Signal=User)
def create_user_profile(Signal, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, Signal=User)
def save_user_profile(Signal, instance, **kwargs):
    instance.userprofile.save()