from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    '''Custom User Model'''

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    avartar = models.ImageField(null=True, blank=True)
    gender = models.CharField(
        choices = GENDER_CHOICES, max_length=10, null=True, blank=True
    )
    bio = models.TextField(default='', blank=True)