from django.db import models

# Create your models here.

# For custom user to inherit
from django.contrib.auth.models import AbstractUser

# new to create my account page
from django.urls import reverse

# Create Customuser class for custom user db table
class CustomUser(AbstractUser):
    # pass
    # new to create my account page
    dob = models.DateField(
        verbose_name="Date of Birth", null=True, blank=True
    )
    
    def get_absolute_url(self):
        return reverse('my-account')

