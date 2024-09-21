from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=100)
    profile_picture = models.ImageField(upload_to='pics/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='follower')
    following = models.ManyToManyField('self')


    def __str__(self):
        return f"{self.username}"

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
