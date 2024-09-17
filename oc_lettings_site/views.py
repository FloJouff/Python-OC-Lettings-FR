from django.shortcuts import render
# from .models import Letting, Profile


def index(request):
    """OC Lettings Home page"""
    return render(request, "index.html")
