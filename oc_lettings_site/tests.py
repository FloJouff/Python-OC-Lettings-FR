import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
from lettings.models import Address, Letting
from profiles.models import Profile
from oc_lettings_site import views
from django.conf import settings
from django.test import override_settings


client = Client()


@pytest.mark.django_db
class TestErrorPages:
    @override_settings(DEBUG=False)
    def test_404_page(self, client):
        response = client.get("/page-inexistante/")
        assert response.status_code == 200
        assert "text/html" in response["Content-Type"]
        assert "404.html" in [t.name for t in response.templates]

    def test_500_page(self, client):
        def raise_error(request):
            raise Exception("Test 500 error")

        from oc_lettings_site import views

        original_index = views.index
        views.index = raise_error

        try:
            response = client.get(reverse("index"))
            assert response.status_code == 200
            assert "500" in response.content.decode()
        finally:
            views.index = original_index

    def test_404_content(self, client):
        response = client.get("/page-inexistante/")
        assert "Error 404 - Page not found" in response.content.decode()

    def test_500_content(self, client):
        def raise_error(request):
            raise Exception("Test 500 error")

        from oc_lettings_site import views

        original_index = views.index
        views.index = raise_error

        try:
            response = client.get(reverse("index"))
            assert "500" in response.content.decode()
        finally:
            views.index = original_index


@pytest.mark.django_db
class TestIntegration:

    def test_error_pages_in_user_journey(self, client):
        response = client.get(reverse("index"))
        assert response.status_code == 200

        response = client.get("/page-inexistante/")
        assert response.status_code == 200
        assert "404.html" in [t.name for t in response.templates]

        response = client.get(reverse("index"))
        assert response.status_code == 200

    def test_full_user_journey(self, client):
        address = Address.objects.create(
            number=123,
            street="Test Street",
            city="Test City",
            state="TS",
            zip_code=12345,
            country_iso_code="TST",
        )
        letting = Letting.objects.create(title="Test Letting", address=address)

        user = User.objects.create_user(username="testuser", password="12345")
        Profile.objects.create(user=user, favorite_city="Test City")

        response = client.get(reverse("index"))
        assert response.status_code == 200

        response = client.get(reverse("lettings:index"))
        assert response.status_code == 200
        assert "Test Letting" in str(response.content)

        response = client.get(reverse("lettings:letting", args=[letting.id]))
        assert response.status_code == 200
        assert "Test Letting" in str(response.content)

        response = client.get(reverse("profiles:index"))
        assert response.status_code == 200
        assert "testuser" in str(response.content)

        response = client.get(reverse("profiles:profile", args=[user.username]))
        assert response.status_code == 200
        assert "testuser" in str(response.content)
        assert "Test City" in str(response.content)

    def test_database_relationships(self):
        address = Address.objects.create(
            number=123,
            street="Test Street",
            city="Test City",
            state="TS",
            zip_code=12345,
            country_iso_code="TST",
        )
        letting = Letting.objects.create(title="Test Letting", address=address)

        assert letting.address == address
        assert Address.objects.count() == 1
        assert Letting.objects.count() == 1

        user = User.objects.create_user(username="testuser", password="12345")
        profile = Profile.objects.create(user=user, favorite_city="Test City")

        assert profile.user == user
        assert User.objects.count() == 1
        assert Profile.objects.count() == 1


@pytest.mark.django_db
class TestErrorHandling:
    def test_debug_mode_off(self):
        assert not settings.DEBUG, "DEBUG should be set to False in production"

    def test_custom_error_handlers_configured(self):
        from oc_lettings_site.urls import handler404, handler500

        assert handler404 == views.error_404
        assert handler500 == views.error_500
