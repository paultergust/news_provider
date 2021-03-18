from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.


class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    objects = UserManager()


class Author(models.Model):
    name = models.CharField(max_length=30)
    picture = models.CharField(max_length=30)



class Article(models.Model):
    category = models.CharField(max_length=2000)
    title = models.CharField(max_length=2000)
    summary = models.CharField(max_length=2000)
    firstParagraph = models.TextField()
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
