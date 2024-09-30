"""
oc_lettings_site/views.py

Contains the Django view's functions related to oc_lettings_site app
(Home page and 404 and 500 error pages)


"""

from django.shortcuts import render
import sentry_sdk
import logging
from sentry_sdk import set_tag

logger = logging.getLogger(__name__)

# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie quam lobortis leo
# consectetur ullamcorper non id est. Praesent dictum, nulla eget feugiat sagittis,
# sem mi convallis eros, vitae dapibus nisi lorem dapibus sem.
# Maecenas pharetra purus ipsum, eget consequat ipsum lobortis quis.
# Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus. Nullam elementum urna nisi,
# pellentesque iaculis enim cursus in. Praesent volutpat porttitor magna,
# non finibus neque cursus id.


def index(request):
    """OC Lettings Home page
    Args:
        request (HttpRequest): the HttpRequest Object

    Returns:
        HttpResponse: HTML page for Home page
    """
    return render(request, "index.html")


def error_404(request, exception):
    """Display custom page in case of error 404

    Args:
        request (HttpRequest): the HttpRequest Object
        exception (exception): Raise an exception in case of error 404

    Returns:
        HttpResponse: HTML page for error 404 page
    """
    logger.error("An error occured: Page not found")
    set_tag("Home", "page not found")
    sentry_sdk.capture_message("Page not found", level="Warning")
    return render(request, "404.html")


def error_500(request):
    """Display custom page in case of error 500

    Args:
        request (HttpRequest): the HttpRequest Object

    Returns:
        HttpResponse: HTML page for error 500 page
    """
    logger.error("Something went wrong with server")
    set_tag("Home", "server error")
    sentry_sdk.capture_message("Something went wrong with server", level="Warning")
    return render(request, "500.html")
