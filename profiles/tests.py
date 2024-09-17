import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile
from django.test import Client


client = Client()


@pytest.mark.django_db
class TestProfiles:
    def test_profile_model(self):
        user = User.objects.create_user(username="testuser", password="12345")
        profile = Profile.objects.create(user=user, favorite_city="Test City")
        assert str(profile) == "testuser"

    def test_profiles_index_view(self, client):
        url = reverse("profiles:index")
        response = client.get(url)
        assert response.status_code == 200
        assert "profiles/index.html" in [t.name for t in response.templates]

    def test_profile_detail_view(self, client):
        user = User.objects.create_user(username="testuser", password="12345")
        Profile.objects.create(user=user, favorite_city="Test City")
        url = reverse("profiles:profile", args=[user.username])
        response = client.get(url)
        assert response.status_code == 200
        assert "profiles/profile.html" in [t.name for t in response.templates]
        assert "testuser" in str(response.content)
