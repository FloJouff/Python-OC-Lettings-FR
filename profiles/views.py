"""
profiles/views.py

contains the Django view's functions related to profiles models

"""

from django.shortcuts import render
from .models import Profile
import logging
from django.http import Http404
from sentry_sdk import set_tag, capture_exception


logger = logging.getLogger(__name__)

# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex,
# sed consequat libero pulvinar eget. Fusc faucibus, urna quis auctor pharetra,
# massa dolor cursus neque, quis dictum lacus d


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

# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate.
# Sed tincidunt, dolor id facilisis fringilla, eros leo tristique lacus,
# it. Nam aliquam dignissim congue.
# Pellentesque habitant morbi tristique senectus et netus et males


def profile(request, username):
    """User's Profile

    Args:
        request (HttpRequest): the HttpRequest Object
        username (str): profile's username

    Return:
        HttpResponse: HTML page for user's profile page
        404.html page in case of unknown id
    """
    try:
        profile = Profile.objects.get(user__username=username)
        logger.info("Loading successful")
    except Exception as e:
        logger.error(f"An error occured: {str(e)}")
        set_tag("Profil", f"User tried to access {username} profile, unsuccessfully")
        capture_exception(e)
        raise Http404("Profile not found")
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
