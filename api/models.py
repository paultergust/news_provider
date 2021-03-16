from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.


class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
