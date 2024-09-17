import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
from lettings.models import Address, Letting
from profiles.models import Profile


client = Client()


@pytest.mark.django_db
class TestOCLettingsSite:
    def test_index_view(self, client):
        url = reverse("index")
        response = client.get(url)
        assert response.status_code == 200
        assert "index.html" in [t.name for t in response.templates]

    def test_custom_404_view(self, client):
        response = client.get("/non-existent-page/")
        assert response.status_code == 404
        assert "404.html" in [t.name for t in response.templates]

    def test_custom_500_view(self):
        # This test requires mocking a server error
        # You might need to create a view that deliberately raises an exception
        pass


@pytest.mark.django_db
class TestIntegration:
    def test_full_user_journey(self, client):
        # Create a letting
        address = Address.objects.create(
            number=123,
            street="Test Street",
            city="Test City",
            state="TS",
            zip_code=12345,
            country_iso_code="TST",
        )
        letting = Letting.objects.create(title="Test Letting", address=address)

        # Create a user and profile
        user = User.objects.create_user(username="testuser", password="12345")
        Profile.objects.create(user=user, favorite_city="Test City")

        # Test main index page
        response = client.get(reverse("index"))
        assert response.status_code == 200

        # Test lettings index page
        response = client.get(reverse("lettings:index"))
        assert response.status_code == 200
        assert "Test Letting" in str(response.content)

        # Test letting detail page
        response = client.get(reverse("lettings:letting", args=[letting.id]))
        assert response.status_code == 200
        assert "Test Letting" in str(response.content)

        # Test profiles index page
        response = client.get(reverse("profiles:index"))
        assert response.status_code == 200
        assert "testuser" in str(response.content)

        # Test profile detail page
        response = client.get(reverse("profiles:profile", args=[user.username]))
        assert response.status_code == 200
        assert "testuser" in str(response.content)
        assert "Test City" in str(response.content)

    def test_database_relationships(self):
        # Create address and letting
        address = Address.objects.create(
            number=123,
            street="Test Street",
            city="Test City",
            state="TS",
            zip_code=12345,
            country_iso_code="TST",
        )
        letting = Letting.objects.create(title="Test Letting", address=address)

        # Verify relationship
        assert letting.address == address
        assert Address.objects.count() == 1
        assert Letting.objects.count() == 1

        # Create user and profile
        user = User.objects.create_user(username="testuser", password="12345")
        profile = Profile.objects.create(user=user, favorite_city="Test City")

        # Verify relationship
        assert profile.user == user
        assert User.objects.count() == 1
        assert Profile.objects.count() == 1
