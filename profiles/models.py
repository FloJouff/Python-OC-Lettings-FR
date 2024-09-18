"""profiles/app.py

This module contains models for the 'profiles' app.
Defines the structures for Profile models in database
"""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Define Profile models

    Attributes
        user(User): ForeignKey related to User model
        favorite_city(str): User's favorite city


    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
