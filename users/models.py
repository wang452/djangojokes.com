from django.db import models

# Create your models here.

# For custom user to inherit
from django.contrib.auth.models import AbstractUser

# Create Customuser class for custom user db table
class CustomUser(AbstractUser):
    pass
