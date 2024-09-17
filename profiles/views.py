from django.shortcuts import render
from .models import Profile


def index(request):
    """Profiles index"""
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """User's Profile

    Args:
        request (_type_): request
        username (str): profile's username

    """
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
