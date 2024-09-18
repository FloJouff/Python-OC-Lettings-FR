"""
lettings/models.py

This module contains models for the 'lettings' app.
Defines the structures for Adress and Letting models in database
"""

from django.db import models


class Address(models.Model):
    """Define Address Models

    Attributes:
        number(int): Streeet number
        street(str): Street's name
        city(str): City's name
        state(str): State for the adress(limited to 2 char)
        zip_code(int): City's Zip code
        country_iso_code(str): ISO code for country (limited to 3 char)

    """
    number = models.PositiveIntegerField()
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2)
    zip_code = models.PositiveIntegerField()
    country_iso_code = models.CharField(max_length=3)

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """Define Letting Model

    Attributes:
        title(str): Letting's title
        address(str): ForeignKey, related to Adress

    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
