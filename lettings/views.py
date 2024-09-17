from django.shortcuts import render
from .models import Letting


def index(request):
    """Index page for lettings"""
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """Page for letting whose id is letting_id

    Args:
        request (_type_): request
        letting_id (int): letting's id

    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
