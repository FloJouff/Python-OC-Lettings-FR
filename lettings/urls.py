"""
lettings/urls.py

Contains the URL patterns for the 'lettings' app,
mapping URL paths to their corresponding view functions.

"""

from django.urls import path
from . import views

app_name = "lettings"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:letting_id>/", views.letting, name="letting"),
]
