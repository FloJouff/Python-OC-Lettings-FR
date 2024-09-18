"""
profiles/views.py

contains the Django view's functions related to profiles models

"""

from django.shortcuts import render
from .models import Profile


def index(request):
    """Profiles index

    Args:
        request (HttpRequest): the HttpRequest Object

    Return:
        HttpResponse: HTML page for profile's index page
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """User's Profile

    Args:
        request (HttpRequest): the HttpRequest Object
        username (str): profile's username

    Return:
        HttpResponse: HTML page for user's profile page
    """
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
