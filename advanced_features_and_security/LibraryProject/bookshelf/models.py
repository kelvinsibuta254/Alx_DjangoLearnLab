from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField("date published")

# class Choice(models.Model):
#     Question = models.ForeignKey(
#         Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField(default=0)

# overide the email fild
#override username field
#create a user manager
#register the user model with django admin
class UserManager(BaseUserManager):
    def create_user(self, email, password):
        #validated the email
        if not email:
            raise ValueError("Users must have an email")
        
        #fetched the user i.e. current model instance
        user = self.model(email=self.normalize_email(email))
        #setting password for the user
        user.set_password(password)
        #saves the password using current database
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()
    email = models.EmailField(unique=True, max_length=255, verbose_name="Email Address")
    username = models.CharField(unique=False, max_length=10)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()