from django.db import models
from django.contrib.auth.models import User as AuthUser

class User(AuthUser):
    ra = models.CharField(
        primary_key = True,
        max_length = 6,
    )
