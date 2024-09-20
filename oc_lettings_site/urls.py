"""
oc_lettings_site/urls.py

Contains the URL pattends for the 'oc_lettings_site' app,
mapping URL paths to their corresponding view functions.
Handles 404 and 500 error.
Redirects on lettings and profiles urls on home page
"""

from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", include("lettings.urls", namespace="lettings")),
    path("profiles/", include("profiles.urls", namespace="profiles")),
    path("admin/", admin.site.urls),
]

handler404 = views.error_404
handler500 = views.error_500
