from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError("email is required")
        user = self.model(email = self.normalize_email(email))
        user.set_password(password)
        user.save(using=self_.db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    username = models.CharField(max_length=20)
    objects = UserManager
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)