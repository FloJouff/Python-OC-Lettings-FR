"""
profiles/urls.py

Contains the URL patterns for the 'profiles' app,
mapping URL paths to their corresponding view functions.

"""

from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:username>/", views.profile, name="profile"),
]
