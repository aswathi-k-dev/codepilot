from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):

    phone = models.CharField(max_length=12,unique=True)

    ROLE_CHOICES = (
        ("student","student"),
        ("admin","admin")
    )

    role = models.CharField(max_length=200,choices=ROLE_CHOICES,default="student")
