"""
lettings/views.py

contains the Django view's functions related to lettings models

"""

from django.shortcuts import render
from .models import Letting
import logging
from sentry_sdk import set_tag, capture_exception

logger = logging.getLogger(__name__)


def index(request):
    """Index page for lettings

    Args:
        request (HttpRequest): the HttpRequest Object

    Return:
        HttpResponse: HTML page for lettings index page
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """Page for letting whose id is letting_id

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
        return render(request, "404.html")
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
