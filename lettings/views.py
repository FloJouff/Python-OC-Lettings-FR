"""
lettings/views.py

contains the Django view's functions related to lettings models

"""

from django.shortcuts import render
from .models import Letting
import logging
from django.http import Http404
from sentry_sdk import set_tag, capture_exception

logger = logging.getLogger(__name__)

# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit.
# Sed non placerat massa. Integer est nunc, pulvinar a tempor et, bibendum id arcu.
# Vestibulum ante ipsum primis in faucibus orci luctus et ultrices
# posuere cubilia curae; Cras eget scelerisque


def index(request):
    """
    Index page for lettings

    Args:
        request (HttpRequest): the HttpRequest Object

    Return:
        HttpResponse: HTML page for lettings index page
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non.
# In accumsan porta nisl id eleifend. Praesent dignissim, odio eu consequat pretium,
# purus urna vulputate arcu, vitae efficitur
#  lacus justo nec purus. Aenean finibus faucibus lectus at porta. Maecenas auctor,
# est ut luctus congue, dui enim mattis enim, ac condimentum velit libero in magna.
# Suspendisse potenti. In tempus a nisi sed laoreet.
# Suspendisse porta dui eget sem accumsan interdum. Ut quis urna pellentesque justo
# mattis ullamcorper ac non tellus. In tristique mauris eu velit fermentum,
# tempus pharetra est luctus. Vivamus consequat aliquam libero, eget bibendum lorem.
# Sed non dolor risus. Mauris condimentum auctor elementum. Donec quis nisi ligula.
# Integer vehicula tincidunt enim, ac lacinia augue pulvinar sit


def letting(request, letting_id):
    """
    Page for letting whose id is letting_id

    Args:
        request (HttpRequest): the HttpRequest Object
        letting_id (int): letting's id

    Return:
        HttpResponse: HTML page for letting page

    """
    try:
        letting = Letting.objects.get(id=letting_id)
        logger.info("Operation successful")
    except Exception as e:
        logger.error(f"An error occured: {str(e)}")
        set_tag("letting", f"User tried to access {letting_id}, unsuccessfully")
        capture_exception(e)
        raise Http404("Letting not found")
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
