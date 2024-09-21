from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User, AbstractUser, BaseUserManager, AbstractBaseUser

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email: 
            raise ValueError("Email is required")
            user = self.model(email=normalize_email(email))
            user.set_password(password)
            user.save(using=self._db)
            return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using= self._db)
        return user

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    username = models.CharField(unique=True, max_length=10)
    bio = models.TextField(max_length=100)
    profile_picture = models.ImageField(upload_to='pics/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='follower')
    following = models.ManyToManyField('self')
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.username}"

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
# class User(AbstractUser):
#     bio = models.TextField(max_length=100)
#     profile_picture = models.URLField()
#     followers = models.ManyToManyField(settings.AUTH_USER_MODEL, symmetrical=False)