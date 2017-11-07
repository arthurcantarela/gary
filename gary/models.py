from django.db import models
from django.contrib.auth.models import User as AuthUser

class User(AuthUser):
    ra = models.CharField(
        primary_key = True,
        max_length = 6,
    )

class Status(models.Model):
    picture = models.BooleanField(
        blank = False,
        null = False,
        default = False
    )
