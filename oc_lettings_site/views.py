"""
oc_lettings_site/views.py

Contains the Django view's functions related to oc_lettings_site app
(Home page and 404 and 500 error pages)


"""

from django.shortcuts import render


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
    return render(request, "404.html")


def error_500(request):
    """Display custom page in case of error 500

    Args:
        request (HttpRequest): the HttpRequest Object

    Returns:
        HttpResponse: HTML page for error 500 page
    """
    return render(request, "500.html")
