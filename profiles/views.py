"""
profiles/views.py

contains the Django view's functions related to profiles models

"""

from django.shortcuts import render
from .models import Profile
import logging
from sentry_sdk import set_tag, capture_exception


logger = logging.getLogger(__name__)


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
    try:
        profile = Profile.objects.get(user__username=username)
        logger.info("Loading successful")
    except Exception as e:
        logger.error(f"An error occured: {str(e)}")
        set_tag("Profil", f"User tried to access {username} profile, unsuccessfully")
        capture_exception(e)
        return render(request, "404.html")
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
